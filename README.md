[![Netlify Status](https://api.netlify.com/api/v1/badges/a0351602-c43c-4095-bf42-f96bf30aa0bc/deploy-status)](https://app.netlify.com/sites/themagiclab/deploys)

# Magic Lab Website

Static site generator for university research lab website.

Site generator: [Hexo](https://hexo.io/)

Editing interface: [Netlify CMS](https://www.netlifycms.org/)

Access control: GitHub account. See allowed collaborators [here](https://github.com/uts-magic-lab/www.themagiclab.org/settings/collaboration).

### Content Management

Navigate to [/admin](https://themagiclab.netlify.com/admin/) and log in with your GitHub account.

### Development

1. Clone this project.

2. Install [Node.js](http://nodejs.org/download/) and run
    
        npm install

    from the project directory.

3. Run

        npm run watch

    and navigate to [http://localhost:4000/](http://localhost:4000/)

    Changes you make to `.pug` templates in `themes/` and `.md` files in `source/` will update the preview automatically.
