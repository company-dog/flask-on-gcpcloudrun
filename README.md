# Flask Restful Api on GCP CodeRun

[![Run on Google Cloud](https://storage.googleapis.com/cloudrun/button.svg)](https://console.cloud.google.com/cloudshell/editor?shellonly=true&cloudshell_image=gcr.io/cloudrun/button&cloudshell_git_repo=https://github.com/company-dog/flask-coderun.git)

## Deploy to CodeRun using CloudBuild

以下有効にする必要がある。

- CloudRun API
- CloudBuild からの CloudRun 実行

```
gcloud builds submit --config cloudbuild.yaml
```
