

//list folders 
//build catalog 

const { lstatSync, readdirSync } = require('fs')
const { basename, join } = require('path')
const kefir = require('kefir');
const _ =  require('lodash');
const YAML = require('yamljs');
const Mustache = require('mustache');
const fs = require('fs');
const debug = require('debug');

const pluginsDir = process.env.PLUGINS  || "../plugins"
debug(`plugins path is ${pluginsDir}`);
const isDirectory = source => lstatSync(source).isDirectory()
const getDirectories = source =>
  readdirSync(source)
  .map(name => join(source, name)).filter(isDirectory);
const getContent = source =>
  readdirSync(source)
  .map(name => join(source, name))

const validatePlugin = (p)=>{return p;}
const catalog = "dynamic-catalog.md";

  let plugins = kefir.sequentially(0,  getDirectories(pluginsDir)).map(validatePlugin)
 
  
const createMD = (template , data)=>{
    Mustache.parse(template);   // optional, speeds up future uses
    data.date = new Date();
    var rendered = Mustache.render(template, data);
    return rendered;
}
 
  let pluginData = plugins.flatMap((plugin)=>{
     let yaml = _.chain(getContent(plugin)).map((f)=>{
        
         return f;
     }).thru((f)=>{
         return f;
     }).filter((file)=>
     (basename(file) === "plugin.yaml"))
         .first().value();
    let pluginMeta;
    try{
        pluginMeta =  YAML.load(yaml)
    }catch(e){
      return kefir.constantError(e)
    }
    return  (_.isUndefined(yaml)) ? kefir.never() : kefir.constant(pluginMeta)
    
    }).ignoreErrors().scan((plugins , p)=>{
        plugins.push(p);
        return plugins;
    }, []).spy().last()
     
    let template = kefir.fromNodeCallback(_.partial(fs.readFile, template))
    .map((f)=>new Buffer(f).toString()).spy();
   

    kefir.concat([template, pluginData]).scan((prev, next)=>{
       prev.push(next);
       return prev;
    }, []).last().spy('->').map((data)=>{
        let t = _.first(data);
        let plugins = _.last(data);
       // plugins = {"plugins": [{image:"1"}, {"image":"2"}]}
        return createMD(t, {plugins});
   }).flatMap((data)=>{
       return kefir.fromNodeCallback(
       _.partial(fs.writeFile, catalog, data)
       )  
    }).log();
 
   