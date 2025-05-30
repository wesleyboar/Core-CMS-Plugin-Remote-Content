# Loading News from TACC Websites

This guide explains how to load news content from [TACC] or other [TACC/Core-CMS]–based websites using this plugin.

[TACC]: https://tacc.utexas.edu
[TACC/Core-CMS]: https://github.com/TACC/Core-CMS

1. [Basics](#basics)
2. [Filter](#filter)
3. [Styles](#styles)
4. [Scripts](#scripts)

## Basics

1. Add a "Remote Content" plugin instance.
2. Set path to:

    ```
    /news/latest-news/?template=plain.html
    ```

    - `/news/latest-news/` is typical, but verify exact path on the source site.
    - `?template=plain.html` removes header, footer, breadcrumbs, assets, etc.

3. Ensure source website has `('plain.html', 'Plain')` in its `CMS_TEMPLATES` setting e.g.

    ```py
    CMS_TEMPLATES = (
        # standard templates, plus...
        ('plain.html', 'Plain'),
    )
    ```

    <sup>This will remove the header, footer, breadcrumbs, global assets, et cetera from the page.</sup>

4. Ensure the pagination links retain their relative URLs, so news list remains inside client:

    ```py
    PORTAL_PLUGIN_CONTENT_USE_RELATIVE_PATHS = [
        '.pagination a' # for "?page=2" links in news lists
    ]
    ```

    <sup>The plugin will forward content parameters (like `page=2`) to the source website, but filter out Django CMS parameters (like `toolbar_on`).</sup>

5. **If** the source website for your news is not [TACC], **then** set the base URL in your settings:

    ```py
    PORTAL_PLUGIN_CONTENT_NETLOC = 'https://example.com/'
    ```

## Filter

You can filter news content by using appropiate path.

| Filter by | Path |
| - | - |
| Tag | `/news/latest-news/tag/SOME_TAG?template=plain.html` |
| Category | `/news/latest-news/category/SOME_CATEGORY?template=plain.html` |

## Styles

The news is styled by a specific stylesheet, [`blog.app.css`](https://github.com/TACC/Core-CMS/blob/v4.29.1/taccsite_cms/static/site_cms/css/src/_imports/components/django.cms.blog.app.css).

- It is **automatically** loaded on [TACC/Core-CMS] **if** the Django CMS setting `STORAGES` is **not** set to `ManifestStaticFilesStorage`.
- It **must be manually** loaded **if** the Django CMS setting `STORAGES` **is** set to `ManifestStaticFilesStorage` (like on [TACC]).

Also, any extra styles must be supplied by the client.

### Add Styles

You can add styles using [djangocms-snippet](https://github.com/django-cms/djangocms-snippet) e.g.

- **Name**: CSS: Blog (as Remote Content)
- **HTML**:

    ```html
    <style id="css-blog-as-remote-content">
    @import url("/static/site_cms/css/build/app.blog.css") layer(project);
    </style>
    ```

- **Slug**: `css-blog-as-remote-content`

## Scripts

Some news content may require JavaScript for certain enhancements.

- If some source articles (like on [TACC]) should link to external news sources, you **must manually** load JavaScript to support that.

Also, any extra scripts must be supplied by the client.

### Add Scripts

You can add scripts using [djangocms-snippet](https://github.com/django-cms/djangocms-snippet) e.g.

- **Name**: JS: Blog (as Remote Content)
- **HTML**: _(see [TUP-UI redirect snippet](https://github.com/TACC/tup-ui/blob/v1.1.15/apps/tup-cms/src/taccsite_cms/templates/snippets/redirect.html))_
- **Slug**: `js-for-blog-as-remote-content`
