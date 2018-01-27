# Security Scanning Tools [![Codefresh build status]( https://g.codefresh.io/api/badges/build?repoOwner=SC-TechDev&repoName=docker-security-scanner&branch=master&pipelineName=docker-security-scanner&accountName=sctechdevservice&type=cf-1)]( https://g.codefresh.io/repositories/SC-TechDev/docker-security-scanner/builds?filter=trigger:build;branch:master;service:59e62c5410e3d100019e7f3d~docker-security-scanner)

Docker image which invokes security script using TwistCLI (Nexus coming soon)

### Prerequisites:

Codefresh Subscription (Dedicated Infrastructure) - https://codefresh.io/

Twistlock Subscription - https://www.twistlock.com/

### Documentation:

Twistlock CLI: https://twistlock.desk.com/customer/en/portal/articles/2875595-twistcli?b_id=16619

Nexus IQ CLI: TBD

## Script Library

### twistlock.py

Executes TwistCLI to scan Docker image given.

### options

To use an ENVIRONMENT VARIABLE you need to add the variables to your Codefresh Pipeline and also to your codefresh.yaml.


Example `codefresh.yml` build is below with required ENVIRONMENT VARIABLES in place.


| ENVIRONMENT VARIABLE | SCRIPT ARGUMENT | DEFAULT | TYPE | REQUIRED | DESCRIPTION |
|----------------------------|--------------------------------------|----------|---------|----------|---------------------------------------------------------------------------------------------------------------------------------|
| CF_METADATA | [ -c, --cf_metadata ] | null | boolean | No | In combination with TL_UPLOAD stores Twistlock Report URL in TL_REPORT_URL var for Codefresh metadata annotation |
| TL_CONSOLE_HOSTNAME | [ -C, --tl_console_hostname ] | null | string | Yes | hostname/ip |
| TL_CONSOLE_PORT | [ -P, --tl_console_port ] | null | string | Yes | port |
| TL_CONSOLE_USERNAME | [ -U, --tl_console_username ] | null | string | Yes | username |
| TL_CONSOLE_PASSWORD | [ -X, --tl_console_password ] | null | string | Yes | password |
| TL_ONLY | [ -Z, --tl_only ] | null | boolean | Yes | Twistlock Console Only (Required for now Nexus TBD) |
| TL_TLS_ENABLED | [ -T, --tl_tls_enabled ] | null | boolean | No | enable TLS |
| TL_HASH | [ -H, --tl_hash ] | [ sha1 ] | string | No | [ md5, sha1, sha256 ] hashing algorithm |
| TL_UPLOAD | [ -R, --tl_upload ] | null | boolean | No | ( ignores all options below if set and only returns report url ) uploads report to Twistlock to be used later via Twistlock API |
| TL_DETAILS | [ -D, --tl_details ] | null | boolean | No | prints an itemized list of each vulnerability found by the scanner |
| TL_ONLY_FIXED | [ -O, --tl_only_fixed ] | null | boolean | No | reports just the vulnerabilites that have fixes available |
| TL_COMPLIANCE_THRESHOLD | [ -M, --tl_compliance_threshold ] | null | string | No | [ low, medium, high ] sets the the minimal severity compliance issue that returns a fail exit code |
| TL_VULNERABILITY_THRESHOLD | [ -V, --tl_vulnerability_threshold ] | null | string | No | [ low, medium, high, critical ] sets the minimal severity vulnerability that returns a fail exit code |

### codefresh.yml

Codefresh Build Step to execute Twistlock scan.
All `${{var}}` variables must be put into Codefresh Build Parameters
codefresh.yml
```console
  buildimage:
    type: build
    title: Build Runtime Image
    dockerfile: Dockerfile
    image_name: # Image you're building/scanning [repository/image]
    tag: latest-cf-build-candidate

  nexus_iq_scan_build_stage:
    type: composition
    composition:
      version: '2'
      services:
        imagebuild:
          image: ${{buildimage}}
          command: sh -c "exit 0"
          labels:
            build.image.id: ${{CF_BUILD_ID}}
    composition_candidates:
      scan_service:
        image: sctechdev/docker-security-scanner
        environment:
          - TL_CONSOLE_HOSTNAME=${{TL_CONSOLE_HOSTNAME}}
          - TL_CONSOLE_PORT=${{TL_CONSOLE_PORT}}
          - TL_CONSOLE_USERNAME=${{TL_CONSOLE_USERNAME}}
          - TL_CONSOLE_PASSWORD=${{TL_CONSOLE_PASSWORD}}
          - TL_ONLY=${{TL_ONLY}}
        command: twistlock.py -i "$$(docker inspect $$(docker inspect $$(docker ps -aqf label=build.image.id=${{CF_BUILD_ID}}) -f {{.Config.Image}}) -f {{.Id}} | sed 's/sha256://g')"
        depends_on:
          - imagebuild
        volumes:
          - /var/run/docker.sock:/var/run/docker.sock
          - /var/lib/docker:/var/lib/docker
          # Everything below this line is Optional for CF_METADATA
          - '${{CF_VOLUME_NAME}}:/codefresh/volume'
    add_flow_volume_to_composition: true

  export:
    title: "Exporting variables..."
    image: alpine
    commands:
      - echo "Exporting variables..."

  set_metadata:
    title: "Setting metadata on image..."
    image: alpine
    commands:
      - echo "Setting metadata on image..."
    on_finish:
      metadata:
        set:
          - '${{build_step.imageId}}':
              - TwistlockSecurityReport: ${{TL_REPORT_URL}}
```