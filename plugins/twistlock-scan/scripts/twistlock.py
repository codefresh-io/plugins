import sys
import subprocess
import time
import os
import getopt
import ssl
import re

def main(argv):
  try:
    st_scanner_jar = '/packages/nexus-iq-cli-1.38.0-02.jar'
    tl_scanner_exec = '/packages/twistcli'
    cf_metadata = os.environ.get('CF_METADATA')
    docker_image_id = os.environ.get('DOCKER_IMAGE_ID')
    st_application_id = os.environ.get('NEXUS_IQ_APPLICATION_ID')
    st_url = os.environ.get('NEXUS_IQ_URL')
    st_username = os.environ.get('NEXUS_IQ_USERNAME')
    st_password = os.environ.get('NEXUS_IQ_PASSWORD')
    st_stage = os.environ.get('NEXUS_IQ_STAGE', 'Build')
    tl_console_hostname = os.environ.get('TL_CONSOLE_HOSTNAME')
    tl_console_port = os.environ.get('TL_CONSOLE_PORT')
    tl_console_username = os.environ.get('TL_CONSOLE_USERNAME')
    tl_console_password = os.environ.get('TL_CONSOLE_PASSWORD')
    tl_only = os.environ.get('TL_ONLY')
    tl_tls_enabled = os.environ.get('TL_TLS_ENABLED')
    tl_hash = os.environ.get('TL_HASH', 'sha1')
    tl_include_package_files = os.environ.get('TL_INCLUDE_PACKAGE_FILES')
    tl_upload = os.environ.get('TL_UPLOAD')
    tl_details = os.environ.get('TL_DETAILS')
    tl_only_fixed = os.environ.get('TL_ONLY_FIXED')
    tl_compliance_threshold = os.environ.get('TL_COMPLIANCE_THRESHOLD')
    tl_vulnerability_threshold = os.environ.get('TL_VULNERABILITY_THRESHOLD')
    java_home = os.environ.get('JAVA_HOME', '/usr/lib/jvm/java-8-openjdk-amd64')
    java_keystore_password = os.environ.get('JAVA_KEYSTORE_PASSWORD', 'changeit')
    opts, args = getopt.getopt(argv,"h:c:i:a:j:u:p:s:t:E:C:P:U:X:Z:J:K:T:H:F:R:D:O:M:V:",
      ["help", "docker_image_id=", "cf_metadata", "st_application_id=", "st_scanner_jar=", "st_url=", "st_username=", "st_password=", "st_stage=",
        "tl_scanner_exec=", "tl_console_hostname", "tl_console_port", "tl_console_username=", "tl_console_password=", "tl_only",
        "tl_tls_enabled", "tl_hash", "tl_include_package_files", "tl_upload", "tl_details", "tl_only_fixed", "tl_compliance_threshold",
        "tl_vulnerability_threshold", "java_home=", "java_keystore_password"
      ]
    )
  except getopt.GetoptError:
    print('Unrecognized Argument! See arguments list using -h or --help. Ex. twistlock.py --help')
    sys.exit(2)
  for opt, arg in opts:
    if opt == ("h","--help"):
      print('twistlock.py --arg value or twistlock.py -a value')
      print('-c --cf_metadata - Adds scanner info to Docker image metadata for Codefresh builds')
      print('-i --docker_image_id [DOCKER_IMAGE_ID] - Docker Image ID short or long IDs accepted')
      print('-a --st_application_id [NEXUS_IQ_APPLICATION_ID] - Applications ID in Nexus IQ')
      print('-j --st_scanner_jar - Location of nexus-iq-cli*.jar file')
      print('-u --st_username [NEXUS_IQ_USERNAME] - Nexus IQ Username')
      print('-p --st_password [NEXUS_IQ_PASSWORD] - Password for Nexus IQ Username')
      print('-s --st_url [NEXUS_IQ_URL] - Sonatype URL must be HTTPS with Valid Cert')
      print('-t --st_stage [NEXUS_IQ_STAGE] - Sonatype Stage')
      print('-E --tl_scanner_exec - Location of twistlock-scanner executable')
      print('-C --tl_console_hostname [TL_CONSOLE_HOSTNAME] - Hostname/IP for Twistlock Console')
      print('-P --tl_console_port [TL_CONSOLE_PORT] - Twistock Console port')
      print('-U --tl_console_username [TL_CONSOLE_USERNAME] - Twistlock Console Username')
      print('-X --tl_console_password [TL_CONSOLE_PASSWORD] - Password for Twistlock Console Username')
      print('-Z --tl_only [TL_ONLY] - Run a stand-alone Twistlock scan')
      print('-T --tl_tls_enabled [TL_TLS_ENABLED] - Enabled TLS/HTTPS for Twistlock scan')
      print('-H --tl_hash [TL_HASH] - Specifies the hashing algorithm. Supported values are md5, sha1, and sha256')
      print('-F --tl_include_package_files [TL_INCLUDE_PACKAGE_FILES] - List all packages in the image')
      print('-R --tl_upload [TL_UPLOAD] - Whether to upload the scan result')
      print('-D --tl_details [TL_DETAILS] - Prints an itemized list of each vulnerability found by the scanner')
      print('-O --tl_only_fixed [TL_ONLY_FIXED] - Reports just the vulnerabilities that have fixes available')
      print('-M --tl_compliance_threshold [TL_COMPLIANCE_THRESHOLD] - Sets the minimum severity compliance issue that returns a fail exit code')
      print('-V --tl_vulnerability_threshold [TL_VULNERABILITY_THRESHOLD] - Sets the minimum severity vulnerability that returns a fail exit code')
      print('-J --java_home [JAVA_HOME] - Java Home Directory (no trailing /)')
      print('-K --java_keystore_password [JAVA_KEYSTORE_PASSWORD] - Java Keystore Password')
      sys.exit()
    elif opt in ("-c", "--cf_metadata"):
      cf_metadata = arg
    elif opt in ("-i", "--docker_image_id"):
      docker_image_id = arg
    elif opt in ("-a", "--st_application_id"):
      st_application_id = arg
    elif opt in ("-j", "--st_scanner_jar"):
      st_scanner_jar = arg
    elif opt in ("-s", "--st_url"):
      st_url = arg
    elif opt in ("-u", "--st_username"):
      st_username = arg
    elif opt in ("-p", "--st_password"):
      st_password = arg
    elif opt in ("-t", "--st_stage"):
      st_stage = arg
    elif opt in ("-E", "--tl_scanner_exec"):
      tl_scanner_exec = arg
    elif opt in ("-C", "--tl_console_hostname"):
      tl_console_hostname = arg
    elif opt in ('-P', "--tl_console_port"):
      tl_console_port = arg
    elif opt in ("-U", "--tl_console_username"):
      tl_console_username = arg
    elif opt in ('-X', "--tl_console_password"):
      tl_console_password = arg
    elif opt in ('-Z', "--tl_only"):
      tl_only = arg
    elif opt in ('-T', "--tl_tls_enabled"):
      tl_tls_enabled = arg
    elif opt in ('-H', "--tl_hash"):
      tl_hash = arg
    elif opt in ('-F', "--tl_include_package_files"):
      tl_include_package_files = arg
    elif opt in ('-R', "--tl_upload"):
      tl_upload = arg
    elif opt in ('-D', "--tl_details"):
      tl_details = arg
    elif opt in ('-O', "--tl_only_fixed"):
      tl_only_fixed = arg
    elif opt in ('-M', "--tl_compliance_threshold"):
      tl_compliance_threshold = arg
    elif opt in ('-V', "--tl_vulnerability_threshold"):
      tl_vulnerability_threshold = arg
    elif opt in ('-J', "--java_home"):
      java_home = arg
    elif opt in ('-K', "--java_keystore_password"):
      java_keystore_password = arg

  # Determine if TLS is required
  if not (tl_only or tl_tls_enable):  
    # Download and store Twistlock Console site cert
    cert = ssl.get_server_certificate((tl_console_hostname, tl_console_port))
    cert, file=open("twistlock.cer", "w")
  
  # Run stand-alone Twistlock Scan
  if tl_only: 
    
    # Determine Protocol
    tl_console_protocol = 'https' if tl_tls_enabled else 'http'
    
    # Base twistcli commnad to scan images
    twistcli_base_command = '/packages/twistcli images scan'
    
    # Required twistcli options to successfully scan image
    twistcli_required_options = ("--address '{}://{}:{}' --user '{}' --password '{}' --hash '{}'"
      .format(tl_console_protocol, tl_console_hostname, tl_console_port, tl_console_username, tl_console_password, tl_hash))

    # Optional twistcli options
    options = []
    if tl_include_package_files: 
      options.append("--include-package-files")
    if tl_upload: 
      options.append("--upload")
    if tl_details: 
      options.append("--details")
    if tl_compliance_threshold: 
      options.append("--compliance-threshold '{}'".format(tl_compliance_threshold))
    if tl_vulnerability_threshold: 
      options.append("--vulnerability-threshold '{}'".format(tl_vulnerability_threshold))
    twistcli_optional_options = ' '.join(options)

    # Concatenate twistcli executable with command
    twistcli_exec = ' '.join([twistcli_base_command, twistcli_required_options, twistcli_optional_options, docker_image_id])
    # Execute command but pipe stdout to variable and parse for Twistlock URL
    if cf_metadata:
      proc = subprocess.Popen(twistcli_exec, shell=True, stdout=subprocess.PIPE)
      stdout = proc.communicate()[0].decode('utf-8').strip('\n')
      tl_report_url = ''.join(re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', stdout))
      with open('/codefresh/volume/env_vars_to_export', 'a') as f:
        print('Twistlock Report: ' + tl_report_url)
        f.write('TL_REPORT_URL=' + tl_report_url)
        f.close()
    # Execute command and send stdout to console
    else:
      proc = subprocess.Popen(twistcli_exec, shell=True)
      stdout, stderr = proc.communicate()
    if proc.returncode != 0:
      sys.exit(1)

  else:
    
    # Import site cert into java keystore
    command = ['keytool -importcert -noprompt -file twistlock.cer -alias twistlock -storepass {} -keystore {}/jre/lib/security/cacerts'
      .format(java_keystore_password, java_home)
    ]
    proc = subprocess.Popen(command, shell=True)
    stdout, stderr = proc.communicate()

    # Start Docker
    command = ['for i in {1..5}; do service docker start && break || sleep 15; done']
    proc = subprocess.Popen(command, shell=True)
    stdout, stderr = proc.communicate()
        
    # Run Twistlock Scan and send file to Sonatype
    command = ["java -cp {} com.sonatype.insight.scan.cli.TwistlockPolicyEvaluatorCli -i {} -a '{}:{}' -s '{}' --twistlock-scanner-executable {} --twistlock-console-url https://{}:{} --twistlock-console-username {} --twistlock-console-password '{}' --stage '{}' {}"
      .format(st_scanner_jar, st_application_id, st_username, st_password, st_url, tl_scanner_exec, tl_console_hostname, tl_console_port, tl_console_username, tl_console_password, st_stage, docker_image_id)
    ]
    proc = subprocess.Popen(command, shell=True)
    stdout, stderr = proc.communicate()

if __name__ == "__main__":
  main(sys.argv[1:])