



<!DOCTYPE html>
<html lang="en" class="">
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# object: http://ogp.me/ns/object# article: http://ogp.me/ns/article# profile: http://ogp.me/ns/profile#">
    <meta charset='utf-8'>

    <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/frameworks-47d5165116e276b4456a8a0b540547bf2e3b64700c9837e254bf69c85f37a08b.css" media="all" rel="stylesheet" />
    <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/github-8c88f419e1fe6938f18d31874b82102d0a4897c7d903452887232cc1f907ddc1.css" media="all" rel="stylesheet" />
    
    
    <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/site-0996ced1a40a04be84d932b2c830830a2c87259cfb5c41c90ca7fee0c5979e9d.css" media="all" rel="stylesheet" />
    

    <link as="script" href="https://assets-cdn.github.com/assets/frameworks-25b3467536f8dbde9085ca7626397da95a8852904d5daf9c274a8a6135e71af1.js" rel="preload" />
    
    <link as="script" href="https://assets-cdn.github.com/assets/github-81cea7d452fde4e34e68317538577bcfd65bac063b330f5f416556e470884c0d.js" rel="preload" />

    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta http-equiv="Content-Language" content="en">
    <meta name="viewport" content="width=device-width">
    
    
    <title>osf.io/tests.py at 13f44b72a34ec1cdffd6df6efe1bd9419dc2084a · acshi/osf.io · GitHub</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
    <link rel="apple-touch-icon" href="/apple-touch-icon.png">
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-57x57.png">
    <link rel="apple-touch-icon" sizes="60x60" href="/apple-touch-icon-60x60.png">
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-72x72.png">
    <link rel="apple-touch-icon" sizes="76x76" href="/apple-touch-icon-76x76.png">
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114x114.png">
    <link rel="apple-touch-icon" sizes="120x120" href="/apple-touch-icon-120x120.png">
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144x144.png">
    <link rel="apple-touch-icon" sizes="152x152" href="/apple-touch-icon-152x152.png">
    <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon-180x180.png">
    <meta property="fb:app_id" content="1401488693436528">

      <meta content="https://avatars1.githubusercontent.com/u/1449974?v=3&amp;s=400" name="twitter:image:src" /><meta content="@github" name="twitter:site" /><meta content="summary" name="twitter:card" /><meta content="acshi/osf.io" name="twitter:title" /><meta content="osf.io - Facilitating Open Science" name="twitter:description" />
      <meta content="https://avatars1.githubusercontent.com/u/1449974?v=3&amp;s=400" property="og:image" /><meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="acshi/osf.io" property="og:title" /><meta content="https://github.com/acshi/osf.io" property="og:url" /><meta content="osf.io - Facilitating Open Science" property="og:description" />
      <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">
    <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">
    <link rel="assets" href="https://assets-cdn.github.com/">
    
    <meta name="pjax-timeout" content="1000">
    

    <meta name="msapplication-TileImage" content="/windows-tile.png">
    <meta name="msapplication-TileColor" content="#ffffff">
    <meta name="selected-link" value="repo_source" data-pjax-transient>

    <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
<meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA">
    <meta name="google-analytics" content="UA-3769691-2">

<meta content="collector.githubapp.com" name="octolytics-host" /><meta content="github" name="octolytics-app-id" /><meta content="C63A6ED7:BDC6:123266:575AE536" name="octolytics-dimension-request_id" />
<meta content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-pjax-transient="true" name="analytics-location" />



  <meta class="js-ga-set" name="dimension1" content="Logged Out">



        <meta name="hostname" content="github.com">
    <meta name="user-login" content="">

        <meta name="expected-hostname" content="github.com">
      <meta name="js-proxy-site-detection-payload" content="OGJkMzVkYTRlNWQyMTEwOTdiMWRjNGE4NTMwMDU5MTYzYjdlNDU1NGYyZTJlY2I2YmRkY2NmYmIzZWEwNmU1Mnx7InJlbW90ZV9hZGRyZXNzIjoiMTk4LjU4LjExMC4yMTUiLCJyZXF1ZXN0X2lkIjoiQzYzQTZFRDc6QkRDNjoxMjMyNjY6NTc1QUU1MzYiLCJ0aW1lc3RhbXAiOjE0NjU1NzQ3MTB9">


      <link rel="mask-icon" href="https://assets-cdn.github.com/pinned-octocat.svg" color="#4078c0">
      <link rel="icon" type="image/x-icon" href="https://assets-cdn.github.com/favicon.ico">

    <meta name="html-safe-nonce" content="d17c67dab36cb0deb106d5fcdcde79a3eeb8923a">
    <meta content="7369ed071a4f41ec29f841d66861954c9b749a2c" name="form-nonce" />

    <meta http-equiv="x-pjax-version" content="207277450bcd1be91c845836fe72cae6">
    

      
  <meta name="description" content="osf.io - Facilitating Open Science">
  <meta name="go-import" content="github.com/acshi/osf.io git https://github.com/acshi/osf.io.git">

  <meta content="1449974" name="octolytics-dimension-user_id" /><meta content="acshi" name="octolytics-dimension-user_login" /><meta content="59302069" name="octolytics-dimension-repository_id" /><meta content="acshi/osf.io" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="true" name="octolytics-dimension-repository_is_fork" /><meta content="10199599" name="octolytics-dimension-repository_parent_id" /><meta content="CenterForOpenScience/osf.io" name="octolytics-dimension-repository_parent_nwo" /><meta content="10199599" name="octolytics-dimension-repository_network_root_id" /><meta content="CenterForOpenScience/osf.io" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/acshi/osf.io/commits/13f44b72a34ec1cdffd6df6efe1bd9419dc2084a.atom" rel="alternate" title="Recent Commits to osf.io:13f44b72a34ec1cdffd6df6efe1bd9419dc2084a" type="application/atom+xml">


      <link rel="canonical" href="https://github.com/acshi/osf.io/blob/13f44b72a34ec1cdffd6df6efe1bd9419dc2084a/framework/discourse/tests.py" data-pjax-transient>
  </head>


  <body class="logged-out   env-production  vis-public fork page-blob">
    <div id="js-pjax-loader-bar" class="pjax-loader-bar"></div>
    <a href="#start-of-content" tabindex="1" class="accessibility-aid js-skip-to-content">Skip to content</a>

    
    
    



          <header class="site-header js-details-container" role="banner">
  <div class="container-responsive">
    <a class="header-logo-invertocat" href="https://github.com/" aria-label="Homepage" data-ga-click="(Logged out) Header, go to homepage, icon:logo-wordmark">
      <svg aria-hidden="true" class="octicon octicon-mark-github" height="32" version="1.1" viewBox="0 0 16 16" width="32"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"></path></svg>
    </a>

    <button class="btn-link right site-header-toggle js-details-target" type="button" aria-label="Toggle navigation">
      <svg aria-hidden="true" class="octicon octicon-three-bars" height="24" version="1.1" viewBox="0 0 12 16" width="18"><path d="M11.41 9H.59C0 9 0 8.59 0 8c0-.59 0-1 .59-1H11.4c.59 0 .59.41.59 1 0 .59 0 1-.59 1h.01zm0-4H.59C0 5 0 4.59 0 4c0-.59 0-1 .59-1H11.4c.59 0 .59.41.59 1 0 .59 0 1-.59 1h.01zM.59 11H11.4c.59 0 .59.41.59 1 0 .59 0 1-.59 1H.59C0 13 0 12.59 0 12c0-.59 0-1 .59-1z"></path></svg>
    </button>

    <div class="site-header-menu">
      <nav class="site-header-nav site-header-nav-main">
        <a href="/personal" class="js-selected-navigation-item nav-item nav-item-personal" data-ga-click="Header, click, Nav menu - item:personal" data-selected-links="/personal /personal">
          Personal
</a>        <a href="/open-source" class="js-selected-navigation-item nav-item nav-item-opensource" data-ga-click="Header, click, Nav menu - item:opensource" data-selected-links="/open-source /open-source">
          Open source
</a>        <a href="/business" class="js-selected-navigation-item nav-item nav-item-business" data-ga-click="Header, click, Nav menu - item:business" data-selected-links="/business /business/features /business/customers /business">
          Business
</a>        <a href="/explore" class="js-selected-navigation-item nav-item nav-item-explore" data-ga-click="Header, click, Nav menu - item:explore" data-selected-links="/explore /trending /trending/developers /integrations /integrations/feature/code /integrations/feature/collaborate /integrations/feature/ship /explore">
          Explore
</a>      </nav>

      <div class="site-header-actions">
            <a class="btn btn-primary site-header-actions-btn" href="/join?source=header-repo" data-ga-click="(Logged out) Header, clicked Sign up, text:sign-up">Sign up</a>
          <a class="btn site-header-actions-btn mr-2" href="/login?return_to=%2Facshi%2Fosf.io%2Fblob%2F13f44b72a34ec1cdffd6df6efe1bd9419dc2084a%2Fframework%2Fdiscourse%2Ftests.py" data-ga-click="(Logged out) Header, clicked Sign in, text:sign-in">Sign in</a>
      </div>

        <nav class="site-header-nav site-header-nav-secondary">
          <a class="nav-item" href="/pricing">Pricing</a>
          <a class="nav-item" href="/blog">Blog</a>
          <a class="nav-item" href="https://help.github.com">Support</a>
          <a class="nav-item header-search-link" href="https://github.com/search">Search GitHub</a>
              <div class="header-search scoped-search site-scoped-search js-site-search" role="search">
  <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/acshi/osf.io/search" class="js-site-search-form" data-scoped-search-url="/acshi/osf.io/search" data-unscoped-search-url="/search" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
    <label class="form-control header-search-wrapper js-chromeless-input-container">
      <div class="header-search-scope">This repository</div>
      <input type="text"
        class="form-control header-search-input js-site-search-focus js-site-search-field is-clearable"
        data-hotkey="s"
        name="q"
        placeholder="Search"
        aria-label="Search this repository"
        data-unscoped-placeholder="Search GitHub"
        data-scoped-placeholder="Search"
        tabindex="1"
        autocapitalize="off">
    </label>
</form></div>

        </nav>
    </div>
  </div>
</header>



    <div id="start-of-content" class="accessibility-aid"></div>

      <div id="js-flash-container">
</div>


    <div role="main" class="main-content">
        <div itemscope itemtype="http://schema.org/SoftwareSourceCode">
    <div id="js-repo-pjax-container" data-pjax-container>
      
<div class="pagehead repohead instapaper_ignore readability-menu experiment-repo-nav">
  <div class="container repohead-details-container">

    

<ul class="pagehead-actions">

  <li>
      <a href="/login?return_to=%2Facshi%2Fosf.io"
    class="btn btn-sm btn-with-count tooltipped tooltipped-n"
    aria-label="You must be signed in to watch a repository" rel="nofollow">
    <svg aria-hidden="true" class="octicon octicon-eye" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"></path></svg>
    Watch
  </a>
  <a class="social-count" href="/acshi/osf.io/watchers">
    1
  </a>

  </li>

  <li>
      <a href="/login?return_to=%2Facshi%2Fosf.io"
    class="btn btn-sm btn-with-count tooltipped tooltipped-n"
    aria-label="You must be signed in to star a repository" rel="nofollow">
    <svg aria-hidden="true" class="octicon octicon-star" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74z"></path></svg>
    Star
  </a>

    <a class="social-count js-social-count" href="/acshi/osf.io/stargazers">
      0
    </a>

  </li>

  <li>
      <a href="/login?return_to=%2Facshi%2Fosf.io"
        class="btn btn-sm btn-with-count tooltipped tooltipped-n"
        aria-label="You must be signed in to fork a repository" rel="nofollow">
        <svg aria-hidden="true" class="octicon octicon-repo-forked" height="16" version="1.1" viewBox="0 0 10 16" width="10"><path d="M8 1a1.993 1.993 0 0 0-1 3.72V6L5 8 3 6V4.72A1.993 1.993 0 0 0 2 1a1.993 1.993 0 0 0-1 3.72V6.5l3 3v1.78A1.993 1.993 0 0 0 5 15a1.993 1.993 0 0 0 1-3.72V9.5l3-3V4.72A1.993 1.993 0 0 0 8 1zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3 10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3-10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
        Fork
      </a>

    <a href="/acshi/osf.io/network" class="social-count">
      187
    </a>
  </li>
</ul>

    <h1 class="public ">
  <svg aria-hidden="true" class="octicon octicon-repo-forked" height="16" version="1.1" viewBox="0 0 10 16" width="10"><path d="M8 1a1.993 1.993 0 0 0-1 3.72V6L5 8 3 6V4.72A1.993 1.993 0 0 0 2 1a1.993 1.993 0 0 0-1 3.72V6.5l3 3v1.78A1.993 1.993 0 0 0 5 15a1.993 1.993 0 0 0 1-3.72V9.5l3-3V4.72A1.993 1.993 0 0 0 8 1zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3 10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3-10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  <span class="author" itemprop="author"><a href="/acshi" class="url fn" rel="author">acshi</a></span><!--
--><span class="path-divider">/</span><!--
--><strong itemprop="name"><a href="/acshi/osf.io" data-pjax="#js-repo-pjax-container">osf.io</a></strong>

    <span class="fork-flag">
      <span class="text">forked from <a href="/CenterForOpenScience/osf.io">CenterForOpenScience/osf.io</a></span>
    </span>
</h1>

  </div>
  <div class="container">
    
<nav class="reponav js-repo-nav js-sidenav-container-pjax"
     itemscope
     itemtype="http://schema.org/BreadcrumbList"
     role="navigation"
     data-pjax="#js-repo-pjax-container">

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a href="/acshi/osf.io" aria-selected="true" class="js-selected-navigation-item selected reponav-item" data-hotkey="g c" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches /acshi/osf.io" itemprop="url">
      <svg aria-hidden="true" class="octicon octicon-code" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path d="M9.5 3L8 4.5 11.5 8 8 11.5 9.5 13 14 8 9.5 3zm-5 0L0 8l4.5 5L6 11.5 2.5 8 6 4.5 4.5 3z"></path></svg>
      <span itemprop="name">Code</span>
      <meta itemprop="position" content="1">
</a>  </span>


  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a href="/acshi/osf.io/pulls" class="js-selected-navigation-item reponav-item" data-hotkey="g p" data-selected-links="repo_pulls /acshi/osf.io/pulls" itemprop="url">
      <svg aria-hidden="true" class="octicon octicon-git-pull-request" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
      <span itemprop="name">Pull requests</span>
      <span class="counter">0</span>
      <meta itemprop="position" content="3">
</a>  </span>



  <a href="/acshi/osf.io/pulse" class="js-selected-navigation-item reponav-item" data-selected-links="pulse /acshi/osf.io/pulse">
    <svg aria-hidden="true" class="octicon octicon-pulse" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path d="M11.5 8L8.8 5.4 6.6 8.5 5.5 1.6 2.38 8H0v2h3.6l.9-1.8.9 5.4L9 8.5l1.6 1.5H14V8z"></path></svg>
    Pulse
</a>
  <a href="/acshi/osf.io/graphs" class="js-selected-navigation-item reponav-item" data-selected-links="repo_graphs repo_contributors /acshi/osf.io/graphs">
    <svg aria-hidden="true" class="octicon octicon-graph" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M16 14v1H0V0h1v14h15zM5 13H3V8h2v5zm4 0H7V3h2v10zm4 0h-2V6h2v7z"></path></svg>
    Graphs
</a>

</nav>

  </div>
</div>

<div class="container new-discussion-timeline experiment-repo-nav">
  <div class="repository-content">

    

<a href="/acshi/osf.io/blob/13f44b72a34ec1cdffd6df6efe1bd9419dc2084a/framework/discourse/tests.py" class="hidden js-permalink-shortcut" data-hotkey="y">Permalink</a>

<!-- blob contrib key: blob_contributors:v21:57ddd09e474fab0a18045b23152f3b1a -->

<div class="file-navigation js-zeroclipboard-container">
  
<div class="select-menu branch-select-menu js-menu-container js-select-menu left">
  <button class="btn btn-sm select-menu-button js-menu-target css-truncate" data-hotkey="w"
    title=""
    type="button" aria-label="Switch branches or tags" tabindex="0" aria-haspopup="true">
    <i>Tree:</i>
    <span class="js-select-button css-truncate-target">13f44b72a3</span>
  </button>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax aria-hidden="true">

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <svg aria-label="Close" class="octicon octicon-x js-menu-close" height="16" role="img" version="1.1" viewBox="0 0 12 16" width="12"><path d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"></path></svg>
        <span class="select-menu-title">Switch branches/tags</span>
      </div>

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Filter branches/tags" id="context-commitish-filter-field" class="form-control js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" data-filter-placeholder="Filter branches/tags" class="js-select-menu-tab" role="tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" data-filter-placeholder="Find a tag…" class="js-select-menu-tab" role="tab">Tags</a>
            </li>
          </ul>
        </div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches" role="menu">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/acshi/osf.io/blob/admin-improvements/framework/discourse/tests.py"
               data-name="admin-improvements"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text" title="admin-improvements">
                admin-improvements
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/acshi/osf.io/blob/develop/framework/discourse/tests.py"
               data-name="develop"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text" title="develop">
                develop
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/acshi/osf.io/blob/feature/multi-institution/framework/discourse/tests.py"
               data-name="feature/multi-institution"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text" title="feature/multi-institution">
                feature/multi-institution
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/acshi/osf.io/blob/feature/new-logs-audit/framework/discourse/tests.py"
               data-name="feature/new-logs-audit"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text" title="feature/new-logs-audit">
                feature/new-logs-audit
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/acshi/osf.io/blob/master/framework/discourse/tests.py"
               data-name="master"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text" title="master">
                master
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/acshi/osf.io/blob/next-major/framework/discourse/tests.py"
               data-name="next-major"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text" title="next-major">
                next-major
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/acshi/osf.io/blob/osf-2052/framework/discourse/tests.py"
               data-name="osf-2052"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text" title="osf-2052">
                osf-2052
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/acshi/osf.io/blob/osf-4553/framework/discourse/tests.py"
               data-name="osf-4553"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text" title="osf-4553">
                osf-4553
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/acshi/osf.io/blob/osf-4556/framework/discourse/tests.py"
               data-name="osf-4556"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text" title="osf-4556">
                osf-4556
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/acshi/osf.io/blob/osf-6397/framework/discourse/tests.py"
               data-name="osf-6397"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text" title="osf-6397">
                osf-6397
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/acshi/osf.io/blob/rnd-discourse/framework/discourse/tests.py"
               data-name="rnd-discourse"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text" title="rnd-discourse">
                rnd-discourse
              </span>
            </a>
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/wikilinks/framework/discourse/tests.py"
              data-name="wikilinks"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="wikilinks">
                wikilinks
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/wiki_metadata/framework/discourse/tests.py"
              data-name="wiki_metadata"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="wiki_metadata">
                wiki_metadata
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/wiki-toc-pointer-url/framework/discourse/tests.py"
              data-name="wiki-toc-pointer-url"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="wiki-toc-pointer-url">
                wiki-toc-pointer-url
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/wiki-preview/framework/discourse/tests.py"
              data-name="wiki-preview"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="wiki-preview">
                wiki-preview
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/wiki-preview-inconsistencies/framework/discourse/tests.py"
              data-name="wiki-preview-inconsistencies"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="wiki-preview-inconsistencies">
                wiki-preview-inconsistencies
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/wiki-preview-inconsistencies-2/framework/discourse/tests.py"
              data-name="wiki-preview-inconsistencies-2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="wiki-preview-inconsistencies-2">
                wiki-preview-inconsistencies-2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/webhook-urls/framework/discourse/tests.py"
              data-name="webhook-urls"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="webhook-urls">
                webhook-urls
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/version-downloads/framework/discourse/tests.py"
              data-name="version-downloads"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="version-downloads">
                version-downloads
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/validate-size-cap/framework/discourse/tests.py"
              data-name="validate-size-cap"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="validate-size-cap">
                validate-size-cap
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/user-profile-fixes/framework/discourse/tests.py"
              data-name="user-profile-fixes"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="user-profile-fixes">
                user-profile-fixes
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/url-for/framework/discourse/tests.py"
              data-name="url-for"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="url-for">
                url-for
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/upload-error-msg/framework/discourse/tests.py"
              data-name="upload-error-msg"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="upload-error-msg">
                upload-error-msg
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/update-email-submission/framework/discourse/tests.py"
              data-name="update-email-submission"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="update-email-submission">
                update-email-submission
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/unwatch-button/framework/discourse/tests.py"
              data-name="unwatch-button"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="unwatch-button">
                unwatch-button
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/unreg-user-profile/framework/discourse/tests.py"
              data-name="unreg-user-profile"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="unreg-user-profile">
                unreg-user-profile
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/unicode_in_str_format/framework/discourse/tests.py"
              data-name="unicode_in_str_format"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="unicode_in_str_format">
                unicode_in_str_format
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/unicode_dulwich/framework/discourse/tests.py"
              data-name="unicode_dulwich"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="unicode_dulwich">
                unicode_dulwich
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/unicode_dulwich_delete/framework/discourse/tests.py"
              data-name="unicode_dulwich_delete"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="unicode_dulwich_delete">
                unicode_dulwich_delete
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/typos/framework/discourse/tests.py"
              data-name="typos"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="typos">
                typos
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/travis/framework/discourse/tests.py"
              data-name="travis"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="travis">
                travis
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/travis-retry/framework/discourse/tests.py"
              data-name="travis-retry"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="travis-retry">
                travis-retry
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/transaction_middleware/framework/discourse/tests.py"
              data-name="transaction_middleware"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="transaction_middleware">
                transaction_middleware
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/tos-pp-footer/framework/discourse/tests.py"
              data-name="tos-pp-footer"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="tos-pp-footer">
                tos-pp-footer
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/things-work-when-search-is-down/framework/discourse/tests.py"
              data-name="things-work-when-search-is-down"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="things-work-when-search-is-down">
                things-work-when-search-is-down
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/tfa-check/framework/discourse/tests.py"
              data-name="tfa-check"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="tfa-check">
                tfa-check
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/tag-guids/framework/discourse/tests.py"
              data-name="tag-guids"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="tag-guids">
                tag-guids
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/swap-gravatar-sizes/framework/discourse/tests.py"
              data-name="swap-gravatar-sizes"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="swap-gravatar-sizes">
                swap-gravatar-sizes
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/support-emails/framework/discourse/tests.py"
              data-name="support-emails"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="support-emails">
                support-emails
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/spsp-dead-link/framework/discourse/tests.py"
              data-name="spsp-dead-link"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="spsp-dead-link">
                spsp-dead-link
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/speedup-session-clearing/framework/discourse/tests.py"
              data-name="speedup-session-clearing"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="speedup-session-clearing">
                speedup-session-clearing
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/skip-malformed-logs/framework/discourse/tests.py"
              data-name="skip-malformed-logs"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="skip-malformed-logs">
                skip-malformed-logs
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/sentry/framework/discourse/tests.py"
              data-name="sentry"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="sentry">
                sentry
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/search_on_small_screens/framework/discourse/tests.py"
              data-name="search_on_small_screens"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="search_on_small_screens">
                search_on_small_screens
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/search-description-ellipses/framework/discourse/tests.py"
              data-name="search-description-ellipses"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="search-description-ellipses">
                search-description-ellipses
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/scriptify-conference-js/framework/discourse/tests.py"
              data-name="scriptify-conference-js"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="scriptify-conference-js">
                scriptify-conference-js
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/s3-serialize-settings/framework/discourse/tests.py"
              data-name="s3-serialize-settings"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="s3-serialize-settings">
                s3-serialize-settings
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/s3-naming/framework/discourse/tests.py"
              data-name="s3-naming"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="s3-naming">
                s3-naming
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/s3-downloads/framework/discourse/tests.py"
              data-name="s3-downloads"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="s3-downloads">
                s3-downloads
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/s3-disabling/framework/discourse/tests.py"
              data-name="s3-disabling"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="s3-disabling">
                s3-disabling
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/s3-bucket-drop-down/framework/discourse/tests.py"
              data-name="s3-bucket-drop-down"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="s3-bucket-drop-down">
                s3-bucket-drop-down
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/s3-auth/framework/discourse/tests.py"
              data-name="s3-auth"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="s3-auth">
                s3-auth
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/rubeus-sorting-none/framework/discourse/tests.py"
              data-name="rubeus-sorting-none"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="rubeus-sorting-none">
                rubeus-sorting-none
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/rubeus-load/framework/discourse/tests.py"
              data-name="rubeus-load"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="rubeus-load">
                rubeus-load
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/rubeus-icons/framework/discourse/tests.py"
              data-name="rubeus-icons"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="rubeus-icons">
                rubeus-icons
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/rm-download-count/framework/discourse/tests.py"
              data-name="rm-download-count"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="rm-download-count">
                rm-download-count
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/revert-pydocx/framework/discourse/tests.py"
              data-name="revert-pydocx"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="revert-pydocx">
                revert-pydocx
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/revert-hotfix-whitespace/framework/discourse/tests.py"
              data-name="revert-hotfix-whitespace"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="revert-hotfix-whitespace">
                revert-hotfix-whitespace
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/restore-css/framework/discourse/tests.py"
              data-name="restore-css"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="restore-css">
                restore-css
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/requirements/framework/discourse/tests.py"
              data-name="requirements"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="requirements">
                requirements
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/reorder_profile_settings/framework/discourse/tests.py"
              data-name="reorder_profile_settings"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="reorder_profile_settings">
                reorder_profile_settings
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/reorder-nodes/framework/discourse/tests.py"
              data-name="reorder-nodes"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="reorder-nodes">
                reorder-nodes
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/remove-contributor/framework/discourse/tests.py"
              data-name="remove-contributor"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="remove-contributor">
                remove-contributor
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/registration_tags/framework/discourse/tests.py"
              data-name="registration_tags"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="registration_tags">
                registration_tags
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/registration-language/framework/discourse/tests.py"
              data-name="registration-language"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="registration-language">
                registration-language
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/registration-help-text/framework/discourse/tests.py"
              data-name="registration-help-text"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="registration-help-text">
                registration-help-text
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/recentactivity/framework/discourse/tests.py"
              data-name="recentactivity"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="recentactivity">
                recentactivity
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/readme/framework/discourse/tests.py"
              data-name="readme"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="readme">
                readme
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/pydocx-version/framework/discourse/tests.py"
              data-name="pydocx-version"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="pydocx-version">
                pydocx-version
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/public-activity-style/framework/discourse/tests.py"
              data-name="public-activity-style"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="public-activity-style">
                public-activity-style
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/project-nav/framework/discourse/tests.py"
              data-name="project-nav"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="project-nav">
                project-nav
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/project-menu-highlight/framework/discourse/tests.py"
              data-name="project-menu-highlight"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="project-menu-highlight">
                project-menu-highlight
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/profile-date-validator/framework/discourse/tests.py"
              data-name="profile-date-validator"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="profile-date-validator">
                profile-date-validator
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/production_flags/framework/discourse/tests.py"
              data-name="production_flags"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="production_flags">
                production_flags
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/private_link/framework/discourse/tests.py"
              data-name="private_link"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="private_link">
                private_link
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/private-registration-label/framework/discourse/tests.py"
              data-name="private-registration-label"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="private-registration-label">
                private-registration-label
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/privacy_log/framework/discourse/tests.py"
              data-name="privacy_log"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="privacy_log">
                privacy_log
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/password-whitespace/framework/discourse/tests.py"
              data-name="password-whitespace"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="password-whitespace">
                password-whitespace
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/parse-upload-error-json/framework/discourse/tests.py"
              data-name="parse-upload-error-json"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="parse-upload-error-json">
                parse-upload-error-json
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/parchive-exceptions/framework/discourse/tests.py"
              data-name="parchive-exceptions"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="parchive-exceptions">
                parchive-exceptions
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/osfstorage-expects/framework/discourse/tests.py"
              data-name="osfstorage-expects"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="osfstorage-expects">
                osfstorage-expects
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/osffiles-urls/framework/discourse/tests.py"
              data-name="osffiles-urls"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="osffiles-urls">
                osffiles-urls
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/optional-rpy2/framework/discourse/tests.py"
              data-name="optional-rpy2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="optional-rpy2">
                optional-rpy2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/nrao-presentation-service/framework/discourse/tests.py"
              data-name="nrao-presentation-service"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="nrao-presentation-service">
                nrao-presentation-service
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/non_ascii_wiki_page_names/framework/discourse/tests.py"
              data-name="non_ascii_wiki_page_names"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="non_ascii_wiki_page_names">
                non_ascii_wiki_page_names
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/node-resolution/framework/discourse/tests.py"
              data-name="node-resolution"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="node-resolution">
                node-resolution
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/node-category/framework/discourse/tests.py"
              data-name="node-category"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="node-category">
                node-category
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/nested-project-script/framework/discourse/tests.py"
              data-name="nested-project-script"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="nested-project-script">
                nested-project-script
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/multi-word-tags-broken/framework/discourse/tests.py"
              data-name="multi-word-tags-broken"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="multi-word-tags-broken">
                multi-word-tags-broken
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/model-reprs/framework/discourse/tests.py"
              data-name="model-reprs"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="model-reprs">
                model-reprs
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/missing-reg-template/framework/discourse/tests.py"
              data-name="missing-reg-template"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="missing-reg-template">
                missing-reg-template
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/migrate_wiki_files_addons/framework/discourse/tests.py"
              data-name="migrate_wiki_files_addons"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="migrate_wiki_files_addons">
                migrate_wiki_files_addons
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/migrate_parents_children/framework/discourse/tests.py"
              data-name="migrate_parents_children"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="migrate_parents_children">
                migrate_parents_children
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/migrate_addons/framework/discourse/tests.py"
              data-name="migrate_addons"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="migrate_addons">
                migrate_addons
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/merged-users-removed-from-search/framework/discourse/tests.py"
              data-name="merged-users-removed-from-search"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="merged-users-removed-from-search">
                merged-users-removed-from-search
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/max-size-warning/framework/discourse/tests.py"
              data-name="max-size-warning"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="max-size-warning">
                max-size-warning
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/mako-string-escaping/framework/discourse/tests.py"
              data-name="mako-string-escaping"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="mako-string-escaping">
                mako-string-escaping
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/mailgun-unicode-error/framework/discourse/tests.py"
              data-name="mailgun-unicode-error"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="mailgun-unicode-error">
                mailgun-unicode-error
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/mail-spam-filter/framework/discourse/tests.py"
              data-name="mail-spam-filter"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="mail-spam-filter">
                mail-spam-filter
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/log-visibility/framework/discourse/tests.py"
              data-name="log-visibility"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="log-visibility">
                log-visibility
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/log-index-error/framework/discourse/tests.py"
              data-name="log-index-error"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="log-index-error">
                log-index-error
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/legal-links/framework/discourse/tests.py"
              data-name="legal-links"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="legal-links">
                legal-links
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/legacy-deploy/framework/discourse/tests.py"
              data-name="legacy-deploy"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="legacy-deploy">
                legacy-deploy
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/issue893/framework/discourse/tests.py"
              data-name="issue893"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="issue893">
                issue893
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/issue833/framework/discourse/tests.py"
              data-name="issue833"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="issue833">
                issue833
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/issue737/framework/discourse/tests.py"
              data-name="issue737"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="issue737">
                issue737
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/issue715/framework/discourse/tests.py"
              data-name="issue715"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="issue715">
                issue715
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/issue662/framework/discourse/tests.py"
              data-name="issue662"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="issue662">
                issue662
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/issue601/framework/discourse/tests.py"
              data-name="issue601"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="issue601">
                issue601
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/issue472/framework/discourse/tests.py"
              data-name="issue472"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="issue472">
                issue472
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/acshi/osf.io/tree/issue-907/framework/discourse/tests.py"
              data-name="issue-907"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target" title="issue-907">
                issue-907
              </span>
            </a>
        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div>

    </div>
  </div>
</div>

  <div class="btn-group right">
    <a href="/acshi/osf.io/find/13f44b72a34ec1cdffd6df6efe1bd9419dc2084a"
          class="js-pjax-capture-input btn btn-sm"
          data-pjax
          data-hotkey="t">
      Find file
    </a>
    <button aria-label="Copy file path to clipboard" class="js-zeroclipboard btn btn-sm zeroclipboard-button tooltipped tooltipped-s" data-copied-hint="Copied!" type="button">Copy path</button>
  </div>
  <div class="breadcrumb js-zeroclipboard-target">
    <span class="repo-root js-repo-root"><span class="js-path-segment"><a href="/acshi/osf.io/tree/13f44b72a34ec1cdffd6df6efe1bd9419dc2084a"><span>osf.io</span></a></span></span><span class="separator">/</span><span class="js-path-segment"><a href="/acshi/osf.io/tree/13f44b72a34ec1cdffd6df6efe1bd9419dc2084a/framework"><span>framework</span></a></span><span class="separator">/</span><span class="js-path-segment"><a href="/acshi/osf.io/tree/13f44b72a34ec1cdffd6df6efe1bd9419dc2084a/framework/discourse"><span>discourse</span></a></span><span class="separator">/</span><strong class="final-path">tests.py</strong>
  </div>
</div>


  <div class="commit-tease">
      <span class="right">
        <a class="commit-tease-sha" href="/acshi/osf.io/commit/8c80199233d00331429b368855118f818ba18a02" data-pjax>
          8c80199
        </a>
        <relative-time datetime="2016-06-09T20:43:02Z">Jun 9, 2016</relative-time>
      </span>
      <div>
        <img alt="" class="avatar" height="20" src="https://0.gravatar.com/avatar/ddf97f2258759706ec9236c5fcdd5c21?d=https%3A%2F%2Fassets-cdn.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png&amp;r=x&amp;s=140" width="20" />
        <span class="user-mention">Acshi Haggenmiller</span>
          <a href="/acshi/osf.io/commit/8c80199233d00331429b368855118f818ba18a02" class="message" data-pjax="true" title="storing discourse ids in the osf db, better syncing of between the two, and better topic creation.">storing discourse ids in the osf db, better syncing of between the tw…</a>
      </div>

    <div class="commit-tease-contributors">
      <button type="button" class="btn-link muted-link contributors-toggle" data-facebox="#blob_contributors_box">
        <strong>0</strong>
         contributors
      </button>
      
    </div>

    <div id="blob_contributors_box" style="display:none">
      <h2 class="facebox-header" data-facebox-id="facebox-header">Users who have contributed to this file</h2>
      <ul class="facebox-user-list" data-facebox-id="facebox-description">
      </ul>
    </div>
  </div>

<div class="file">
  <div class="file-header">
  <div class="file-actions">

    <div class="btn-group">
      <a href="/acshi/osf.io/raw/13f44b72a34ec1cdffd6df6efe1bd9419dc2084a/framework/discourse/tests.py" class="btn btn-sm " id="raw-url">Raw</a>
        <a href="/acshi/osf.io/blame/13f44b72a34ec1cdffd6df6efe1bd9419dc2084a/framework/discourse/tests.py" class="btn btn-sm js-update-url-with-hash">Blame</a>
      <a href="/acshi/osf.io/commits/13f44b72a34ec1cdffd6df6efe1bd9419dc2084a/framework/discourse/tests.py" class="btn btn-sm " rel="nofollow">History</a>
    </div>


        <button type="button" class="btn-octicon disabled tooltipped tooltipped-nw"
          aria-label="You must be signed in to make or propose changes">
          <svg aria-hidden="true" class="octicon octicon-pencil" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path d="M0 12v3h3l8-8-3-3-8 8zm3 2H1v-2h1v1h1v1zm10.3-9.3L12 6 9 3l1.3-1.3a.996.996 0 0 1 1.41 0l1.59 1.59c.39.39.39 1.02 0 1.41z"></path></svg>
        </button>
        <button type="button" class="btn-octicon btn-octicon-danger disabled tooltipped tooltipped-nw"
          aria-label="You must be signed in to make or propose changes">
          <svg aria-hidden="true" class="octicon octicon-trashcan" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M11 2H9c0-.55-.45-1-1-1H5c-.55 0-1 .45-1 1H2c-.55 0-1 .45-1 1v1c0 .55.45 1 1 1v9c0 .55.45 1 1 1h7c.55 0 1-.45 1-1V5c.55 0 1-.45 1-1V3c0-.55-.45-1-1-1zm-1 12H3V5h1v8h1V5h1v8h1V5h1v8h1V5h1v9zm1-10H2V3h9v1z"></path></svg>
        </button>
  </div>

  <div class="file-info">
      69 lines (53 sloc)
      <span class="file-info-divider"></span>
    2.27 KB
  </div>
</div>

  

  <div itemprop="text" class="blob-wrapper data type-python">
      <table class="highlight tab-size js-file-line-container" data-tab-size="8">
      <tr>
        <td id="L1" class="blob-num js-line-number" data-line-number="1"></td>
        <td id="LC1" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> . <span class="pl-k">import</span> <span class="pl-k">*</span></td>
      </tr>
      <tr>
        <td id="L2" class="blob-num js-line-number" data-line-number="2"></td>
        <td id="LC2" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> time</td>
      </tr>
      <tr>
        <td id="L3" class="blob-num js-line-number" data-line-number="3"></td>
        <td id="LC3" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L4" class="blob-num js-line-number" data-line-number="4"></td>
        <td id="LC4" class="blob-code blob-code-inner js-file-line"><span class="pl-c"># http://stackoverflow.com/questions/3335268/are-object-literals-pythonic</span></td>
      </tr>
      <tr>
        <td id="L5" class="blob-num js-line-number" data-line-number="5"></td>
        <td id="LC5" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">literal</span>(<span class="pl-c1">object</span>):</td>
      </tr>
      <tr>
        <td id="L6" class="blob-num js-line-number" data-line-number="6"></td>
        <td id="LC6" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-c1">__init__</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-k">**</span><span class="pl-smi">kwargs</span>):</td>
      </tr>
      <tr>
        <td id="L7" class="blob-num js-line-number" data-line-number="7"></td>
        <td id="LC7" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.<span class="pl-c1">__dict__</span> <span class="pl-k">=</span> kwargs</td>
      </tr>
      <tr>
        <td id="L8" class="blob-num js-line-number" data-line-number="8"></td>
        <td id="LC8" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-c1">__repr__</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L9" class="blob-num js-line-number" data-line-number="9"></td>
        <td id="LC9" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> <span class="pl-s"><span class="pl-pds">&#39;</span>literal(<span class="pl-c1">%s</span>)<span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> <span class="pl-s"><span class="pl-pds">&#39;</span>, <span class="pl-pds">&#39;</span></span>.join(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">%s</span> = <span class="pl-c1">%r</span><span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> i <span class="pl-k">for</span> i <span class="pl-k">in</span> <span class="pl-c1">sorted</span>(<span class="pl-v">self</span>.<span class="pl-c1">__dict__</span>.iteritems()))</td>
      </tr>
      <tr>
        <td id="L10" class="blob-num js-line-number" data-line-number="10"></td>
        <td id="LC10" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-c1">__str__</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L11" class="blob-num js-line-number" data-line-number="11"></td>
        <td id="LC11" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> <span class="pl-c1">repr</span>(<span class="pl-v">self</span>)</td>
      </tr>
      <tr>
        <td id="L12" class="blob-num js-line-number" data-line-number="12"></td>
        <td id="LC12" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L13" class="blob-num js-line-number" data-line-number="13"></td>
        <td id="LC13" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">local_group_test</span>():</td>
      </tr>
      <tr>
        <td id="L14" class="blob-num js-line-number" data-line-number="14"></td>
        <td id="LC14" class="blob-code blob-code-inner js-file-line">    user1 <span class="pl-k">=</span> literal(<span class="pl-v">_id</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>etfhq<span class="pl-pds">&#39;</span></span>, <span class="pl-v">username</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>acshikh@gmail.com<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L15" class="blob-num js-line-number" data-line-number="15"></td>
        <td id="LC15" class="blob-code blob-code-inner js-file-line">    user2 <span class="pl-k">=</span> literal(<span class="pl-v">_id</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>3ktmb<span class="pl-pds">&#39;</span></span>, <span class="pl-v">username</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>acshikh@cos.io<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L16" class="blob-num js-line-number" data-line-number="16"></td>
        <td id="LC16" class="blob-code blob-code-inner js-file-line">    project_node <span class="pl-k">=</span> literal(<span class="pl-v">title</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>The Test Project<span class="pl-pds">&#39;</span></span>, <span class="pl-v">_id</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>test1234<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L17" class="blob-num js-line-number" data-line-number="17"></td>
        <td id="LC17" class="blob-code blob-code-inner js-file-line">                           <span class="pl-v">contributors</span><span class="pl-k">=</span>[user1, user2], <span class="pl-v">is_public</span><span class="pl-k">=</span><span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L18" class="blob-num js-line-number" data-line-number="18"></td>
        <td id="LC18" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L19" class="blob-num js-line-number" data-line-number="19"></td>
        <td id="LC19" class="blob-code blob-code-inner js-file-line">    delete_group(project_node)</td>
      </tr>
      <tr>
        <td id="L20" class="blob-num js-line-number" data-line-number="20"></td>
        <td id="LC20" class="blob-code blob-code-inner js-file-line">    time.sleep(<span class="pl-c1">0.125</span>)</td>
      </tr>
      <tr>
        <td id="L21" class="blob-num js-line-number" data-line-number="21"></td>
        <td id="LC21" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L22" class="blob-num js-line-number" data-line-number="22"></td>
        <td id="LC22" class="blob-code blob-code-inner js-file-line">    sync_group(project_node)</td>
      </tr>
      <tr>
        <td id="L23" class="blob-num js-line-number" data-line-number="23"></td>
        <td id="LC23" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">assert</span> <span class="pl-c1">len</span>(get_group_users(project_node)) <span class="pl-k">==</span> <span class="pl-c1">2</span></td>
      </tr>
      <tr>
        <td id="L24" class="blob-num js-line-number" data-line-number="24"></td>
        <td id="LC24" class="blob-code blob-code-inner js-file-line">    time.sleep(<span class="pl-c1">0.125</span>)</td>
      </tr>
      <tr>
        <td id="L25" class="blob-num js-line-number" data-line-number="25"></td>
        <td id="LC25" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L26" class="blob-num js-line-number" data-line-number="26"></td>
        <td id="LC26" class="blob-code blob-code-inner js-file-line">    project_node.contributors <span class="pl-k">=</span> [user1]</td>
      </tr>
      <tr>
        <td id="L27" class="blob-num js-line-number" data-line-number="27"></td>
        <td id="LC27" class="blob-code blob-code-inner js-file-line">    sync_group(project_node)</td>
      </tr>
      <tr>
        <td id="L28" class="blob-num js-line-number" data-line-number="28"></td>
        <td id="LC28" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">assert</span> <span class="pl-c1">len</span>(get_group_users(project_node)) <span class="pl-k">==</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L29" class="blob-num js-line-number" data-line-number="29"></td>
        <td id="LC29" class="blob-code blob-code-inner js-file-line">    time.sleep(<span class="pl-c1">0.125</span>)</td>
      </tr>
      <tr>
        <td id="L30" class="blob-num js-line-number" data-line-number="30"></td>
        <td id="LC30" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L31" class="blob-num js-line-number" data-line-number="31"></td>
        <td id="LC31" class="blob-code blob-code-inner js-file-line">    project_node.contributors <span class="pl-k">=</span> [user1, user2]</td>
      </tr>
      <tr>
        <td id="L32" class="blob-num js-line-number" data-line-number="32"></td>
        <td id="LC32" class="blob-code blob-code-inner js-file-line">    sync_group(project_node)</td>
      </tr>
      <tr>
        <td id="L33" class="blob-num js-line-number" data-line-number="33"></td>
        <td id="LC33" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">assert</span> <span class="pl-c1">len</span>(get_group_users(project_node)) <span class="pl-k">==</span> <span class="pl-c1">2</span></td>
      </tr>
      <tr>
        <td id="L34" class="blob-num js-line-number" data-line-number="34"></td>
        <td id="LC34" class="blob-code blob-code-inner js-file-line">    time.sleep(<span class="pl-c1">0.125</span>)</td>
      </tr>
      <tr>
        <td id="L35" class="blob-num js-line-number" data-line-number="35"></td>
        <td id="LC35" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L36" class="blob-num js-line-number" data-line-number="36"></td>
        <td id="LC36" class="blob-code blob-code-inner js-file-line">    project_node.contributors <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L37" class="blob-num js-line-number" data-line-number="37"></td>
        <td id="LC37" class="blob-code blob-code-inner js-file-line">    sync_group(project_node)</td>
      </tr>
      <tr>
        <td id="L38" class="blob-num js-line-number" data-line-number="38"></td>
        <td id="LC38" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">assert</span> <span class="pl-c1">len</span>(get_group_users(project_node)) <span class="pl-k">==</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L39" class="blob-num js-line-number" data-line-number="39"></td>
        <td id="LC39" class="blob-code blob-code-inner js-file-line">    time.sleep(<span class="pl-c1">0.125</span>)</td>
      </tr>
      <tr>
        <td id="L40" class="blob-num js-line-number" data-line-number="40"></td>
        <td id="LC40" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L41" class="blob-num js-line-number" data-line-number="41"></td>
        <td id="LC41" class="blob-code blob-code-inner js-file-line">    delete_group(project_node)</td>
      </tr>
      <tr>
        <td id="L42" class="blob-num js-line-number" data-line-number="42"></td>
        <td id="LC42" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">assert</span> get_group_id(project_node) <span class="pl-k">is</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L43" class="blob-num js-line-number" data-line-number="43"></td>
        <td id="LC43" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L44" class="blob-num js-line-number" data-line-number="44"></td>
        <td id="LC44" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>test passed<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L45" class="blob-num js-line-number" data-line-number="45"></td>
        <td id="LC45" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L46" class="blob-num js-line-number" data-line-number="46"></td>
        <td id="LC46" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">local_category_test</span>():</td>
      </tr>
      <tr>
        <td id="L47" class="blob-num js-line-number" data-line-number="47"></td>
        <td id="LC47" class="blob-code blob-code-inner js-file-line">    project_node <span class="pl-k">=</span> literal(<span class="pl-v">title</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>The Test Project<span class="pl-pds">&#39;</span></span>, <span class="pl-v">_id</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>test1234<span class="pl-pds">&#39;</span></span>, <span class="pl-v">is_public</span><span class="pl-k">=</span><span class="pl-c1">True</span>, <span class="pl-v">contributors</span><span class="pl-k">=</span>[])</td>
      </tr>
      <tr>
        <td id="L48" class="blob-num js-line-number" data-line-number="48"></td>
        <td id="LC48" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L49" class="blob-num js-line-number" data-line-number="49"></td>
        <td id="LC49" class="blob-code blob-code-inner js-file-line">    delete_category(project_node)</td>
      </tr>
      <tr>
        <td id="L50" class="blob-num js-line-number" data-line-number="50"></td>
        <td id="LC50" class="blob-code blob-code-inner js-file-line">    create_category(project_node)</td>
      </tr>
      <tr>
        <td id="L51" class="blob-num js-line-number" data-line-number="51"></td>
        <td id="LC51" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">assert</span> get_category_id(project_node) <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L52" class="blob-num js-line-number" data-line-number="52"></td>
        <td id="LC52" class="blob-code blob-code-inner js-file-line">    delete_category(project_node)</td>
      </tr>
      <tr>
        <td id="L53" class="blob-num js-line-number" data-line-number="53"></td>
        <td id="LC53" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">assert</span> get_category_id(project_node) <span class="pl-k">is</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L54" class="blob-num js-line-number" data-line-number="54"></td>
        <td id="LC54" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L55" class="blob-num js-line-number" data-line-number="55"></td>
        <td id="LC55" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>test passed<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L56" class="blob-num js-line-number" data-line-number="56"></td>
        <td id="LC56" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L57" class="blob-num js-line-number" data-line-number="57"></td>
        <td id="LC57" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">local_comment_test</span>():</td>
      </tr>
      <tr>
        <td id="L58" class="blob-num js-line-number" data-line-number="58"></td>
        <td id="LC58" class="blob-code blob-code-inner js-file-line">    user1 <span class="pl-k">=</span> literal(<span class="pl-v">_id</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>etfhq<span class="pl-pds">&#39;</span></span>, <span class="pl-v">username</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>acshikh@gmail.com<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L59" class="blob-num js-line-number" data-line-number="59"></td>
        <td id="LC59" class="blob-code blob-code-inner js-file-line">    project_node <span class="pl-k">=</span> literal(<span class="pl-v">title</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>The Test Project<span class="pl-pds">&#39;</span></span>, <span class="pl-v">_id</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>test1234<span class="pl-pds">&#39;</span></span>, <span class="pl-v">contributors</span><span class="pl-k">=</span>[user1], <span class="pl-v">is_public</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L60" class="blob-num js-line-number" data-line-number="60"></td>
        <td id="LC60" class="blob-code blob-code-inner js-file-line">    file_node <span class="pl-k">=</span> literal(<span class="pl-v">_id</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>573cb78e96f6d02370c991a9<span class="pl-pds">&#39;</span></span>, <span class="pl-v">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>superRickyRobot.jpg<span class="pl-pds">&#39;</span></span>, <span class="pl-v">node</span><span class="pl-k">=</span>project_node)</td>
      </tr>
      <tr>
        <td id="L61" class="blob-num js-line-number" data-line-number="61"></td>
        <td id="LC61" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L62" class="blob-num js-line-number" data-line-number="62"></td>
        <td id="LC62" class="blob-code blob-code-inner js-file-line">    comment_id <span class="pl-k">=</span> create_comment(file_node, <span class="pl-s"><span class="pl-pds">&#39;</span>I think your robot is the coolest little bugger ever!<span class="pl-pds">&#39;</span></span>, user1)</td>
      </tr>
      <tr>
        <td id="L63" class="blob-num js-line-number" data-line-number="63"></td>
        <td id="LC63" class="blob-code blob-code-inner js-file-line">    edit_comment(comment_id, <span class="pl-s"><span class="pl-pds">&#39;</span>Actually, your robot is the coolest little bugger ever!<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L64" class="blob-num js-line-number" data-line-number="64"></td>
        <td id="LC64" class="blob-code blob-code-inner js-file-line">    delete_comment(comment_id)</td>
      </tr>
      <tr>
        <td id="L65" class="blob-num js-line-number" data-line-number="65"></td>
        <td id="LC65" class="blob-code blob-code-inner js-file-line">    undelete_comment(comment_id)</td>
      </tr>
      <tr>
        <td id="L66" class="blob-num js-line-number" data-line-number="66"></td>
        <td id="LC66" class="blob-code blob-code-inner js-file-line">    delete_comment(comment_id)</td>
      </tr>
      <tr>
        <td id="L67" class="blob-num js-line-number" data-line-number="67"></td>
        <td id="LC67" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L68" class="blob-num js-line-number" data-line-number="68"></td>
        <td id="LC68" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>test passed<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
</table>

  </div>

</div>

<button type="button" data-facebox="#jump-to-line" data-facebox-class="linejump" data-hotkey="l" class="hidden">Jump to Line</button>
<div id="jump-to-line" style="display:none">
  <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="" class="js-jump-to-line-form" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
    <input class="form-control linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" aria-label="Jump to line" autofocus>
    <button type="submit" class="btn">Go</button>
</form></div>

  </div>
  <div class="modal-backdrop"></div>
</div>


    </div>
  </div>

    </div>

        <div class="container site-footer-container">
  <div class="site-footer" role="contentinfo">
    <ul class="site-footer-links right">
        <li><a href="https://status.github.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
      <li><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
      <li><a href="https://shop.github.com" data-ga-click="Footer, go to shop, text:shop">Shop</a></li>
        <li><a href="https://github.com/blog" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a href="https://github.com/about" data-ga-click="Footer, go to about, text:about">About</a></li>

    </ul>

    <a href="https://github.com" aria-label="Homepage" class="site-footer-mark" title="GitHub">
      <svg aria-hidden="true" class="octicon octicon-mark-github" height="24" version="1.1" viewBox="0 0 16 16" width="24"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"></path></svg>
</a>
    <ul class="site-footer-links">
      <li>&copy; 2016 <span title="0.12038s from github-fe132-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="https://github.com/site/terms" data-ga-click="Footer, go to terms, text:terms">Terms</a></li>
        <li><a href="https://github.com/site/privacy" data-ga-click="Footer, go to privacy, text:privacy">Privacy</a></li>
        <li><a href="https://github.com/security" data-ga-click="Footer, go to security, text:security">Security</a></li>
        <li><a href="https://github.com/contact" data-ga-click="Footer, go to contact, text:contact">Contact</a></li>
        <li><a href="https://help.github.com" data-ga-click="Footer, go to help, text:help">Help</a></li>
    </ul>
  </div>
</div>



    

    <div id="ajax-error-message" class="ajax-error-message flash flash-error">
      <svg aria-hidden="true" class="octicon octicon-alert" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M8.865 1.52c-.18-.31-.51-.5-.87-.5s-.69.19-.87.5L.275 13.5c-.18.31-.18.69 0 1 .19.31.52.5.87.5h13.7c.36 0 .69-.19.86-.5.17-.31.18-.69.01-1L8.865 1.52zM8.995 13h-2v-2h2v2zm0-3h-2V6h2v4z"></path></svg>
      <button type="button" class="flash-close js-flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
        <svg aria-hidden="true" class="octicon octicon-x" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"></path></svg>
      </button>
      Something went wrong with that request. Please try again.
    </div>


      <script crossorigin="anonymous" src="https://assets-cdn.github.com/assets/compat-7db58f8b7b91111107fac755dd8b178fe7db0f209ced51fc339c446ad3f8da2b.js"></script>
      <script crossorigin="anonymous" src="https://assets-cdn.github.com/assets/frameworks-25b3467536f8dbde9085ca7626397da95a8852904d5daf9c274a8a6135e71af1.js"></script>
      <script async="async" crossorigin="anonymous" src="https://assets-cdn.github.com/assets/github-81cea7d452fde4e34e68317538577bcfd65bac063b330f5f416556e470884c0d.js"></script>
      
      
      
      
      
      
    <div class="js-stale-session-flash stale-session-flash flash flash-warn flash-banner hidden">
      <svg aria-hidden="true" class="octicon octicon-alert" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M8.865 1.52c-.18-.31-.51-.5-.87-.5s-.69.19-.87.5L.275 13.5c-.18.31-.18.69 0 1 .19.31.52.5.87.5h13.7c.36 0 .69-.19.86-.5.17-.31.18-.69.01-1L8.865 1.52zM8.995 13h-2v-2h2v2zm0-3h-2V6h2v4z"></path></svg>
      <span class="signed-in-tab-flash">You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span>
      <span class="signed-out-tab-flash">You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
    </div>
    <div class="facebox" id="facebox" style="display:none;">
  <div class="facebox-popup">
    <div class="facebox-content" role="dialog" aria-labelledby="facebox-header" aria-describedby="facebox-description">
    </div>
    <button type="button" class="facebox-close js-facebox-close" aria-label="Close modal">
      <svg aria-hidden="true" class="octicon octicon-x" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"></path></svg>
    </button>
  </div>
</div>

  </body>
</html>

