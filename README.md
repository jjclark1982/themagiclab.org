[![Netlify Status](https://api.netlify.com/api/v1/badges/a0351602-c43c-4095-bf42-f96bf30aa0bc/deploy-status)](https://app.netlify.com/sites/themagiclab/deploys)

# Magic Lab Website

Static site generator for university research lab website.

Access control is by GitHub account permissions. See allowed collaborators [here](https://github.com/uts-magic-lab/www.themagiclab.org/settings/collaboration).

### Content Management

Navigate to [/admin](https://themagiclab.netlify.com/admin/) and log in with your GitHub account.

##### To create or edit a page

Select the **Pages** Collection on the left-hand side, and select the page or the "New Page" button.

Make your changes and click the "Publish" button. This will upload the page to GitHub.

It should take 30-60 seconds to deploy from GitHub to the content delivery network. Click the status badge at the top of this README for deployment details.

### Development

1. Clone this project.

2. Install [Node.js](http://nodejs.org/download/) and run
    
        npm install

    from the project directory.

3. Run

        npm run watch

    and navigate to [http://localhost:4000/](http://localhost:4000/)

    Changes you make to `.pug` templates in `themes/` and `.md` files in `source/` will update the preview automatically.

- [Hexo site configuration](https://hexo.io/docs/configuration) is in `_config.yml`.

- [Hexo theme configuration](https://hexo.io/docs/themes) is in `themes/magiclab/_config.yml`.

- [Netlify-CMS editor configuration](https://www.netlifycms.org/docs/configuration-options/) is in `source/admin/config.yml`.

##### To add a new type of page

1. Define the schema for the page editor in `source/admin/config.yml`  
    See the documentation on [Collections](https://www.netlifycms.org/docs/configuration-options/#collections) and [Widgets](https://www.netlifycms.org/docs/widgets/) configuration.

2. For collections that do not support creating new pages in the CMS, create the page file somewhere in `source/`, typically as a `.md` file.

3. Specify which template to use in the `layout` field. The default is `page.pug`. You can create additional layout files in `themes/magiclab/layout/`.

4. If desired, you can write preview templates for the CMS in `source/admin/index.html`. (TODO: automatically load the `.pug` files on the admin page.)
