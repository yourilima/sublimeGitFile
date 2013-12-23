sublimeGitFile
==============

open a file in the web interface of github or gitlab

works out of the box with github

for gitlab edit your project.sublime-project (ctrl/cmd-p: Project: edit)
and add the following

```json
{
  [
    'folders': {...}
  ]
  'settings': {
    'opengit':'http://yourgitlabrepo.com'
  }
}
```

