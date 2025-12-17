# Documentation from LaTeX
Demo on how to publish documentation on GitHub Pages using LaTeX and
GitHub Actions.

## Pre-requisites

Enable Pages updates via Actions.

1. Go to repository settings
2. Click on `Code and automation > Pages`
3. In `Build and deployment > Source` select `GitHub Actions`

## Dependencies

- `xu-cheng/latex-action` to easily build LaTeX automatically
    - Set `working_directory` to the documentation folder
    - Set `root_file` to `main.tex`
- `actions/configure-pages`
- `actions/upload-pages-artifact`
- `actions/deploy-pages`

## Permissions

Remember to give permissions to the action like this:

```yml
permissions:
  contents: read
  pages: write
  id-token: write
```

