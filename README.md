# Overview

Front end service for an app.  Written in python using Flask.

## Keys to Datadog Configuration

Datadog provides [Setup Guidance](https://curryware.datadoghq.com/services?env=prod&fromUser=true&selectedEnv=prod&selectedService).  This is a great way to start get started with best practices.

### Using the Datadog [Tracing Libraries](https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/dd_libraries/) on Kubernetes

* Linking source code - the key to this is getting the [CI Pipeline](https://github.com/scotcurry/front-end/tree/master/.github/workflows) correct.  The key code (in the build-actions.yml file) are getting the *org.opencontainers.image.source* and *org.opencontainers.image.revision* labels.
* These are [the manifests](https://github.com/scotcurry/k8-manifests) used for the deployment.
```
- name: Build and Push
        uses: docker/build-push-action@v5
        with:
          context: .
          platforms: linux/amd64,linux/arm64/v8
          push: true
          # Don't forget to set the IMAGE_NAME environment variable.
          tags: scotcurry4/curryware-front-end:${{ github.run_number}}
          labels: |
            org.opencontainers.image.source=github.com/scotcurry/front-end
            org.opencontainers.image.revision=${{ github.sha }}
            tags.datadoghq.com/env=prod
            tags.datadoghq.com/version=${{ github.run_number }}
            tags.datadoghq.com/service=curryware-front-end
```
* Logging - It is important to make sure that they grok parser has the [%{_datadog_prefix}](https://curryware.datadoghq.com/logs/pipelines/pipeline/yJ-trxa8TVS_gCatCCfn5w/processors/edit/lcCftKPPRrCDCwH7EZHnuA) setting and the log file are configured with the [correct format](https://github.com/scotcurry/front-end/blob/master/app.py#L16). 