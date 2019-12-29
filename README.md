# Flask Restful Api on GCP CodeRun

[![Run on Google Cloud](https://storage.googleapis.com/cloudrun/button.svg)](https://console.cloud.google.com/cloudshell/editor?shellonly=true&cloudshell_image=gcr.io/cloudrun/button&cloudshell_git_repo=https://github.com/company-dog/flask-coderun.git)

## API Endpoint

### Create Todo

```
POST /todos
Content-Type: appliation/json

{
  "title": "go to bed at pm.9"
}
```

### Get Todo

```
GET /todo/<todo_id>
```

### Update Todo

```
PUT /todo/<todo_id>
Content-Type: application/json

{
  "title": "go to bed at pm.10",
  "completed": true
}
```

### Delete Todo

```
DELETE /todo/<todo_id>
```

## Manual Deploy to CodeRun using CloudBuild

以下有効にする必要がある。

- CloudRun API
- CloudBuild からの CloudRun 実行

```
gcloud builds submit --config cloudbuild.yaml
```
