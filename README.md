sublimeGitFile
==============

open a file in the web interface of github or gitlab

works out of the box with github with submodules and multiple git repos

for gitlab edit your project.sublime-project (ctrl/cmd-p: Project: edit)
and add the following

```json
{
  "folders":[
    {...}
  ],
  "settings": {
    "gitlab_url":"http://yourgitlabrepo.com"
  }
}
```

