<!DOCTYPE html>
<!-- saved from url=(0045)https://savanna.alxafrica.com/projects/100760 -->
<html lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="">
    <meta name="google" content="notranslate">

      <script type="text/javascript" async="" src="./robust_division_calculator_files/cody-widget.js.download"></script><script type="text/javascript" async="" src="./robust_division_calculator_files/js"></script><script async="" src="./robust_division_calculator_files/pendo.js.download"></script><script async="" src="./robust_division_calculator_files/gtm.js.download"></script><script>
    window.dataLayer = window.dataLayer || [];
    dataLayer.push({"userId":906777,"visitorType":"student","batch":{"id":880,"fullNameWithC":"LOS-BE-0425 (C#5-TL-BE)","schoolLocation":{"id":3,"name":"Lagos"}},"curriculum":{"id":70,"name":"Back-End Web Development"}});

    window.gtm_user_custom_event = function (name, options) {
      if (typeof name === 'undefined') {
        return;
      }

      window.dataLayer.push({
        customEventOptions: typeof options !== 'undefined' ? options : {},
        event: name,
      });
    }
  </script>

  <!-- Google Tag Manager -->
  <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
  new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
  j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
  'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
  })(window,document,'script','dataLayer','GTM-N4C8MF2');</script>
  <!-- End Google Tag Manager -->

      <!-- Pendo -->
  <script>
    (function(apiKey){
      (function(p,e,n,d,o){var v,w,x,y,z;o=p[d]=p[d]||{};o._q=o._q||[];
      v=['initialize','identify','updateOptions','pageLoad','track'];for(w=0,x=v.length;w<x;++w)(function(m){
        o[m]=o[m]||function(){o._q[m===v[0]?'unshift':'push']([m].concat([].slice.call(arguments,0)));};})(v[w]);
        y=e.createElement(n);y.async=!0;y.src='https://cdn.eu.pendo.io/agent/static/'+apiKey+'/pendo.js';
        z=e.getElementsByTagName(n)[0];z.parentNode.insertBefore(y,z);})(window,document,'script','pendo');

        pendo.initialize({"visitor":{"id":"horpehyemmy@gmail.com","email":"horpehyemmy@gmail.com","isLearner":true,"isStaff":false,"prgCohortId":880,"prgCohortName":"LOS-BE-0425 (C#5-TL-BE)","id_svna":906777,"curId_svna":70,"curName_svna":"Back-End Web Development","curCohortId_svna":880,"curCohortName_svna":"LOS-BE-0425 (C#5-TL-BE)","curCohortSchLocName_svna":"Lagos","curCohortSchLocId_svna":3}});
    })('3353b3bd-f678-4388-5809-8944627d3f27');
  </script>
  <!-- End Pendo -->


    <title>Project: Programming Paradigms &amp; Exception handling | Lagos Intranet</title>

      <link rel="stylesheet" href="./robust_division_calculator_files/xgz4ilr.css">
      <link rel="stylesheet" media="all" href="./robust_division_calculator_files/application_alx-2a1e79a71228e50e2741d64f35cdfe6c3a9654fa919707e05b325049cd2c17ef.css">
      <script src="./robust_division_calculator_files/loader.js.download"></script>
      <script src="./robust_division_calculator_files/application-252dcd8508606726f4ddaf4c92f8384f850b9b7ad7705c2a26cb16f060bd1476.js.download"></script>
      <link rel="shortcut icon" type="image/x-icon" href="https://savanna.alxafrica.com/favicon_alx.ico">
      <meta name="csrf-param" content="authenticity_token">
<meta name="csrf-token" content="MbZEk9Zt_pd0dFAneojXgDDavx8XZhb_27PQjj-udMaC_xzTfW7DNqVk4L7o8X49Up97gadcxMfDjlnacIrtew">

      <link rel="apple-touch-icon" href="https://savanna.alxafrica.com/apple-touch-icon_alx.png">

      <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
      <!--[if lt IE 9]>
        <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
        <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
      <![endif]-->

      <!-- Store user timezone -->
      <script>
        Cookies.set('timezone', (new Date()).getTimezoneOffset() / -60.0);
      </script>

        <script src="./robust_division_calculator_files/sdk_styles_v1.0.0.js.download"></script><style>/*
! tailwindcss v3.4.3 | MIT License | https://tailwindcss.com
*//*
1. Prevent padding and border from affecting element width. (https://github.com/mozdevs/cssremedy/issues/4)
2. Allow adding a border to an element by just adding a border-width. (https://github.com/tailwindcss/tailwindcss/pull/116)
*/.sdk *,
.sdk ::before,
.sdk ::after {
  box-sizing: border-box; /* 1 */
  border-width: 0; /* 2 */
  border-style: solid; /* 2 */
  border-color: #e5e7eb; /* 2 */
}.sdk ::before,
.sdk ::after {
  --tw-content: '';
}/*
1. Use a consistent sensible line-height in all browsers.
2. Prevent adjustments of font size after orientation changes in iOS.
3. Use a more readable tab size.
4. Use the user's configured `sans` font-family by default.
5. Use the user's configured `sans` font-feature-settings by default.
6. Use the user's configured `sans` font-variation-settings by default.
7. Disable tap highlights on iOS
*/html,
:host {
  line-height: 1.5; /* 1 */
  -webkit-text-size-adjust: 100%; /* 2 */
  -moz-tab-size: 4; /* 3 */
  -o-tab-size: 4;
     tab-size: 4; /* 3 */
  font-family: Poppins, ui-sans-serif, system-ui, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"; /* 4 */
  font-feature-settings: normal; /* 5 */
  font-variation-settings: normal; /* 6 */
  -webkit-tap-highlight-color: transparent; /* 7 */
}/*
1. Remove the margin in all browsers.
2. Inherit line-height from `html` so users can set them as a class directly on the `html` element.
*/body {
  margin: 0; /* 1 */
  line-height: inherit; /* 2 */
}/*
1. Add the correct height in Firefox.
2. Correct the inheritance of border color in Firefox. (https://bugzilla.mozilla.org/show_bug.cgi?id=190655)
3. Ensure horizontal rules are visible by default.
*/.sdk hr {
  height: 0; /* 1 */
  color: inherit; /* 2 */
  border-top-width: 1px; /* 3 */
}/*
Add the correct text decoration in Chrome, Edge, and Safari.
*/.sdk abbr:where([title]) {
  -webkit-text-decoration: underline dotted;
          text-decoration: underline dotted;
}/*
Remove the default font size and weight for headings.
*/.sdk h1,
.sdk h2,
.sdk h3,
.sdk h4,
.sdk h5,
.sdk h6 {
  font-size: inherit;
  font-weight: inherit;
}/*
Reset links to optimize for opt-in styling instead of opt-out.
*/.sdk a {
  color: inherit;
  text-decoration: inherit;
}/*
Add the correct font weight in Edge and Safari.
*/.sdk b,
.sdk strong {
  font-weight: bolder;
}/*
1. Use the user's configured `mono` font-family by default.
2. Use the user's configured `mono` font-feature-settings by default.
3. Use the user's configured `mono` font-variation-settings by default.
4. Correct the odd `em` font sizing in all browsers.
*/.sdk code,
.sdk kbd,
.sdk samp,
.sdk pre {
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace; /* 1 */
  font-feature-settings: normal; /* 2 */
  font-variation-settings: normal; /* 3 */
  font-size: 1em; /* 4 */
}/*
Add the correct font size in all browsers.
*/.sdk small {
  font-size: 80%;
}/*
Prevent `sub` and `sup` elements from affecting the line height in all browsers.
*/.sdk sub,
.sdk sup {
  font-size: 75%;
  line-height: 0;
  position: relative;
  vertical-align: baseline;
}.sdk sub {
  bottom: -0.25em;
}.sdk sup {
  top: -0.5em;
}/*
1. Remove text indentation from table contents in Chrome and Safari. (https://bugs.chromium.org/p/chromium/issues/detail?id=999088, https://bugs.webkit.org/show_bug.cgi?id=201297)
2. Correct table border color inheritance in all Chrome and Safari. (https://bugs.chromium.org/p/chromium/issues/detail?id=935729, https://bugs.webkit.org/show_bug.cgi?id=195016)
3. Remove gaps between table borders by default.
*/.sdk table {
  text-indent: 0; /* 1 */
  border-color: inherit; /* 2 */
  border-collapse: collapse; /* 3 */
}/*
1. Change the font styles in all browsers.
2. Remove the margin in Firefox and Safari.
3. Remove default padding in all browsers.
*/.sdk button,
.sdk input,
.sdk optgroup,
.sdk select,
.sdk textarea {
  font-family: inherit; /* 1 */
  font-feature-settings: inherit; /* 1 */
  font-variation-settings: inherit; /* 1 */
  font-size: 100%; /* 1 */
  font-weight: inherit; /* 1 */
  line-height: inherit; /* 1 */
  letter-spacing: inherit; /* 1 */
  color: inherit; /* 1 */
  margin: 0; /* 2 */
  padding: 0; /* 3 */
}/*
Remove the inheritance of text transform in Edge and Firefox.
*/.sdk button,
.sdk select {
  text-transform: none;
}/*
1. Correct the inability to style clickable types in iOS and Safari.
2. Remove default button styles.
*/.sdk button,
.sdk input:where([type='button']),
.sdk input:where([type='reset']),
.sdk input:where([type='submit']) {
  -webkit-appearance: button; /* 1 */
  background-color: transparent; /* 2 */
  background-image: none; /* 2 */
}/*
Use the modern Firefox focus style for all focusable elements.
*/.sdk :-moz-focusring {
  outline: auto;
}/*
Remove the additional `:invalid` styles in Firefox. (https://github.com/mozilla/gecko-dev/blob/2f9eacd9d3d995c937b4251a5557d95d494c9be1/layout/style/res/forms.css#L728-L737)
*/.sdk :-moz-ui-invalid {
  box-shadow: none;
}/*
Add the correct vertical alignment in Chrome and Firefox.
*/.sdk progress {
  vertical-align: baseline;
}/*
Correct the cursor style of increment and decrement buttons in Safari.
*/.sdk ::-webkit-inner-spin-button,
.sdk ::-webkit-outer-spin-button {
  height: auto;
}/*
1. Correct the odd appearance in Chrome and Safari.
2. Correct the outline style in Safari.
*/.sdk [type='search'] {
  -webkit-appearance: textfield; /* 1 */
  outline-offset: -2px; /* 2 */
}/*
Remove the inner padding in Chrome and Safari on macOS.
*/.sdk ::-webkit-search-decoration {
  -webkit-appearance: none;
}/*
1. Correct the inability to style clickable types in iOS and Safari.
2. Change font properties to `inherit` in Safari.
*/.sdk ::-webkit-file-upload-button {
  -webkit-appearance: button; /* 1 */
  font: inherit; /* 2 */
}/*
Add the correct display in Chrome and Safari.
*/.sdk summary {
  display: list-item;
}/*
Removes the default spacing and border for appropriate elements.
*/.sdk blockquote,
.sdk dl,
.sdk dd,
.sdk h1,
.sdk h2,
.sdk h3,
.sdk h4,
.sdk h5,
.sdk h6,
.sdk hr,
.sdk figure,
.sdk p,
.sdk pre {
  margin: 0;
}.sdk fieldset {
  margin: 0;
  padding: 0;
}.sdk legend {
  padding: 0;
}.sdk ol,
.sdk ul,
.sdk menu {
  list-style: none;
  margin: 0;
  padding: 0;
}/*
Reset default styling for dialogs.
*/.sdk dialog {
  padding: 0;
}/*
Prevent resizing textareas horizontally by default.
*/.sdk textarea {
  resize: vertical;
}/*
1. Reset the default placeholder opacity in Firefox. (https://github.com/tailwindlabs/tailwindcss/issues/3300)
2. Set the default placeholder color to the user's configured gray 400 color.
*/.sdk input::-moz-placeholder, .sdk textarea::-moz-placeholder {
  opacity: 1; /* 1 */
  color: #9ca3af; /* 2 */
}.sdk input::placeholder,
.sdk textarea::placeholder {
  opacity: 1; /* 1 */
  color: #9ca3af; /* 2 */
}/*
Set the default cursor for buttons.
*/.sdk button,
.sdk [role="button"] {
  cursor: pointer;
}/*
Make sure disabled buttons don't get the pointer cursor.
*/.sdk :disabled {
  cursor: default;
}/*
1. Make replaced elements `display: block` by default. (https://github.com/mozdevs/cssremedy/issues/14)
2. Add `vertical-align: middle` to align replaced elements more sensibly by default. (https://github.com/jensimmons/cssremedy/issues/14#issuecomment-634934210)
   This can trigger a poorly considered lint error in some tools but is included by design.
*/.sdk img,
.sdk svg,
.sdk video,
.sdk canvas,
.sdk audio,
.sdk iframe,
.sdk embed,
.sdk object {
  display: block; /* 1 */
  vertical-align: middle; /* 2 */
}/*
Constrain images and videos to the parent width and preserve their intrinsic aspect ratio. (https://github.com/mozdevs/cssremedy/issues/14)
*/.sdk img,
.sdk video {
  max-width: 100%;
  height: auto;
}/* Make elements with the HTML hidden attribute stay hidden by default */.sdk [hidden] {
  display: none;
}/* latin-ext */@font-face {
    font-family: 'Poppins';
    font-style: normal;
    font-weight: 300;
    font-display: swap;
    src: url(https://fonts.gstatic.com/s/poppins/v21/pxiByp8kv8JHgFVrLDz8Z1JlFd2JQEl8qw.woff2) format('woff2');
    unicode-range: U+0100-02AF, U+0304, U+0308, U+0329, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF;
  }/* latin */@font-face {
    font-family: 'Poppins';
    font-style: normal;
    font-weight: 300;
    font-display: swap;
    src: url(https://fonts.gstatic.com/s/poppins/v21/pxiByp8kv8JHgFVrLDz8Z1xlFd2JQEk.woff2) format('woff2');
    unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
  }/* latin-ext */@font-face {
    font-family: 'Poppins';
    font-style: normal;
    font-weight: 400;
    font-display: swap;
    src: url(https://fonts.gstatic.com/s/poppins/v21/pxiEyp8kv8JHgFVrJJnecnFHGPezSQ.woff2) format('woff2');
    unicode-range: U+0100-02AF, U+0304, U+0308, U+0329, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF;
  }/* latin */@font-face {
    font-family: 'Poppins';
    font-style: normal;
    font-weight: 400;
    font-display: swap;
    src: url(https://fonts.gstatic.com/s/poppins/v21/pxiEyp8kv8JHgFVrJJfecnFHGPc.woff2) format('woff2');
    unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
  }/* latin-ext */@font-face {
    font-family: 'Poppins';
    font-style: normal;
    font-weight: 500;
    font-display: swap;
    src: url(https://fonts.gstatic.com/s/poppins/v21/pxiByp8kv8JHgFVrLGT9Z1JlFd2JQEl8qw.woff2) format('woff2');
    unicode-range: U+0100-02AF, U+0304, U+0308, U+0329, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF;
  }/* latin */@font-face {
    font-family: 'Poppins';
    font-style: normal;
    font-weight: 500;
    font-display: swap;
    src: url(https://fonts.gstatic.com/s/poppins/v21/pxiByp8kv8JHgFVrLGT9Z1xlFd2JQEk.woff2) format('woff2');
    unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
  }/* latin-ext */@font-face {
    font-family: 'Poppins';
    font-style: normal;
    font-weight: 600;
    font-display: swap;
    src: url(https://fonts.gstatic.com/s/poppins/v21/pxiByp8kv8JHgFVrLEj6Z1JlFd2JQEl8qw.woff2) format('woff2');
    unicode-range: U+0100-02AF, U+0304, U+0308, U+0329, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF;
  }/* latin */@font-face {
    font-family: 'Poppins';
    font-style: normal;
    font-weight: 600;
    font-display: swap;
    src: url(https://fonts.gstatic.com/s/poppins/v21/pxiByp8kv8JHgFVrLEj6Z1xlFd2JQEk.woff2) format('woff2');
    unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
  }/* latin-ext */@font-face {
    font-family: 'Poppins';
    font-style: normal;
    font-weight: 700;
    font-display: swap;
    src: url(https://fonts.gstatic.com/s/poppins/v21/pxiByp8kv8JHgFVrLCz7Z1JlFd2JQEl8qw.woff2) format('woff2');
    unicode-range: U+0100-02AF, U+0304, U+0308, U+0329, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF;
  }/* latin */@font-face {
    font-family: 'Poppins';
    font-style: normal;
    font-weight: 700;
    font-display: swap;
    src: url(https://fonts.gstatic.com/s/poppins/v21/pxiByp8kv8JHgFVrLCz7Z1xlFd2JQEk.woff2) format('woff2');
    unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
  }.sdk :focus-visible {
    outline: none;
  }.sdk *, .sdk ::before, .sdk ::after {
  --tw-border-spacing-x: 0;
  --tw-border-spacing-y: 0;
  --tw-translate-x: 0;
  --tw-translate-y: 0;
  --tw-rotate: 0;
  --tw-skew-x: 0;
  --tw-skew-y: 0;
  --tw-scale-x: 1;
  --tw-scale-y: 1;
  --tw-pan-x:  ;
  --tw-pan-y:  ;
  --tw-pinch-zoom:  ;
  --tw-scroll-snap-strictness: proximity;
  --tw-gradient-from-position:  ;
  --tw-gradient-via-position:  ;
  --tw-gradient-to-position:  ;
  --tw-ordinal:  ;
  --tw-slashed-zero:  ;
  --tw-numeric-figure:  ;
  --tw-numeric-spacing:  ;
  --tw-numeric-fraction:  ;
  --tw-ring-inset:  ;
  --tw-ring-offset-width: 0px;
  --tw-ring-offset-color: #fff;
  --tw-ring-color: rgb(59 130 246 / 0.5);
  --tw-ring-offset-shadow: 0 0 #0000;
  --tw-ring-shadow: 0 0 #0000;
  --tw-shadow: 0 0 #0000;
  --tw-shadow-colored: 0 0 #0000;
  --tw-blur:  ;
  --tw-brightness:  ;
  --tw-contrast:  ;
  --tw-grayscale:  ;
  --tw-hue-rotate:  ;
  --tw-invert:  ;
  --tw-saturate:  ;
  --tw-sepia:  ;
  --tw-drop-shadow:  ;
  --tw-backdrop-blur:  ;
  --tw-backdrop-brightness:  ;
  --tw-backdrop-contrast:  ;
  --tw-backdrop-grayscale:  ;
  --tw-backdrop-hue-rotate:  ;
  --tw-backdrop-invert:  ;
  --tw-backdrop-opacity:  ;
  --tw-backdrop-saturate:  ;
  --tw-backdrop-sepia:  ;
  --tw-contain-size:  ;
  --tw-contain-layout:  ;
  --tw-contain-paint:  ;
  --tw-contain-style:  ;
}.sdk ::backdrop {
  --tw-border-spacing-x: 0;
  --tw-border-spacing-y: 0;
  --tw-translate-x: 0;
  --tw-translate-y: 0;
  --tw-rotate: 0;
  --tw-skew-x: 0;
  --tw-skew-y: 0;
  --tw-scale-x: 1;
  --tw-scale-y: 1;
  --tw-pan-x:  ;
  --tw-pan-y:  ;
  --tw-pinch-zoom:  ;
  --tw-scroll-snap-strictness: proximity;
  --tw-gradient-from-position:  ;
  --tw-gradient-via-position:  ;
  --tw-gradient-to-position:  ;
  --tw-ordinal:  ;
  --tw-slashed-zero:  ;
  --tw-numeric-figure:  ;
  --tw-numeric-spacing:  ;
  --tw-numeric-fraction:  ;
  --tw-ring-inset:  ;
  --tw-ring-offset-width: 0px;
  --tw-ring-offset-color: #fff;
  --tw-ring-color: rgb(59 130 246 / 0.5);
  --tw-ring-offset-shadow: 0 0 #0000;
  --tw-ring-shadow: 0 0 #0000;
  --tw-shadow: 0 0 #0000;
  --tw-shadow-colored: 0 0 #0000;
  --tw-blur:  ;
  --tw-brightness:  ;
  --tw-contrast:  ;
  --tw-grayscale:  ;
  --tw-hue-rotate:  ;
  --tw-invert:  ;
  --tw-saturate:  ;
  --tw-sepia:  ;
  --tw-drop-shadow:  ;
  --tw-backdrop-blur:  ;
  --tw-backdrop-brightness:  ;
  --tw-backdrop-contrast:  ;
  --tw-backdrop-grayscale:  ;
  --tw-backdrop-hue-rotate:  ;
  --tw-backdrop-invert:  ;
  --tw-backdrop-opacity:  ;
  --tw-backdrop-saturate:  ;
  --tw-backdrop-sepia:  ;
  --tw-contain-size:  ;
  --tw-contain-layout:  ;
  --tw-contain-paint:  ;
  --tw-contain-style:  ;
}.sdk .container {
  width: 100%;
  margin-right: auto;
  margin-left: auto;
  padding-right: 2rem;
  padding-left: 2rem;
}@media (min-width: 1400px) {.sdk .container {
    max-width: 1400px;
  }
}.sdk .sr-only {
  position: absolute !important;
  width: 1px !important;
  height: 1px !important;
  padding: 0 !important;
  margin: -1px !important;
  overflow: hidden !important;
  clip: rect(0, 0, 0, 0) !important;
  white-space: nowrap !important;
  border-width: 0 !important;
}.sdk .pointer-events-none {
  pointer-events: none !important;
}.sdk .pointer-events-auto {
  pointer-events: auto !important;
}.sdk .visible {
  visibility: visible !important;
}.sdk .invisible {
  visibility: hidden !important;
}.sdk .fixed {
  position: fixed !important;
}.sdk .absolute {
  position: absolute !important;
}.sdk .relative {
  position: relative !important;
}.sdk .inset-0 {
  inset: 0px !important;
}.sdk .inset-x-0 {
  left: 0px !important;
  right: 0px !important;
}.sdk .inset-y-0 {
  top: 0px !important;
  bottom: 0px !important;
}.sdk .-top-6 {
  top: -1.5rem !important;
}.sdk .bottom-0 {
  bottom: 0px !important;
}.sdk .left-0 {
  left: 0px !important;
}.sdk .left-1 {
  left: 0.25rem !important;
}.sdk .left-16 {
  left: 4rem !important;
}.sdk .left-2 {
  left: 0.5rem !important;
}.sdk .left-\[50\%\] {
  left: 50% !important;
}.sdk .right-0 {
  right: 0px !important;
}.sdk .right-1 {
  right: 0.25rem !important;
}.sdk .right-2 {
  right: 0.5rem !important;
}.sdk .right-4 {
  right: 1rem !important;
}.sdk .top-0 {
  top: 0px !important;
}.sdk .top-1\/2 {
  top: 50% !important;
}.sdk .top-10 {
  top: 2.5rem !important;
}.sdk .top-2 {
  top: 0.5rem !important;
}.sdk .top-20 {
  top: 5rem !important;
}.sdk .top-4 {
  top: 1rem !important;
}.sdk .top-\[1px\] {
  top: 1px !important;
}.sdk .top-\[50\%\] {
  top: 50% !important;
}.sdk .top-\[60\%\] {
  top: 60% !important;
}.sdk .top-full {
  top: 100% !important;
}.sdk .z-0 {
  z-index: 0 !important;
}.sdk .z-10 {
  z-index: 10 !important;
}.sdk .z-20 {
  z-index: 20 !important;
}.sdk .z-50 {
  z-index: 50 !important;
}.sdk .z-\[1001\] {
  z-index: 1001 !important;
}.sdk .z-\[1002\] {
  z-index: 1002 !important;
}.sdk .z-\[100\] {
  z-index: 100 !important;
}.sdk .z-\[1\] {
  z-index: 1 !important;
}.sdk .z-\[2\] {
  z-index: 2 !important;
}.sdk .z-\[3\] {
  z-index: 3 !important;
}.sdk .col-span-1 {
  grid-column: span 1 / span 1 !important;
}.sdk .col-span-12 {
  grid-column: span 12 / span 12 !important;
}.sdk .col-span-2 {
  grid-column: span 2 / span 2 !important;
}.sdk .col-span-3 {
  grid-column: span 3 / span 3 !important;
}.sdk .col-span-4 {
  grid-column: span 4 / span 4 !important;
}.sdk .col-span-6 {
  grid-column: span 6 / span 6 !important;
}.sdk .m-2 {
  margin: 0.5rem !important;
}.sdk .-mx-1 {
  margin-left: -0.25rem !important;
  margin-right: -0.25rem !important;
}.sdk .-mx-4 {
  margin-left: -1rem !important;
  margin-right: -1rem !important;
}.sdk .-mx-6 {
  margin-left: -1.5rem !important;
  margin-right: -1.5rem !important;
}.sdk .-my-2 {
  margin-top: -0.5rem !important;
  margin-bottom: -0.5rem !important;
}.sdk .mx-1 {
  margin-left: 0.25rem !important;
  margin-right: 0.25rem !important;
}.sdk .mx-3 {
  margin-left: 0.75rem !important;
  margin-right: 0.75rem !important;
}.sdk .mx-4 {
  margin-left: 1rem !important;
  margin-right: 1rem !important;
}.sdk .mx-auto {
  margin-left: auto !important;
  margin-right: auto !important;
}.sdk .my-1 {
  margin-top: 0.25rem !important;
  margin-bottom: 0.25rem !important;
}.sdk .my-12 {
  margin-top: 3rem !important;
  margin-bottom: 3rem !important;
}.sdk .my-3 {
  margin-top: 0.75rem !important;
  margin-bottom: 0.75rem !important;
}.sdk .my-4 {
  margin-top: 1rem !important;
  margin-bottom: 1rem !important;
}.sdk .my-6 {
  margin-top: 1.5rem !important;
  margin-bottom: 1.5rem !important;
}.sdk .my-8 {
  margin-top: 2rem !important;
  margin-bottom: 2rem !important;
}.sdk .my-auto {
  margin-top: auto !important;
  margin-bottom: auto !important;
}.sdk .\!ml-1 {
  margin-left: 0.25rem !important;
}.sdk .-mr-6 {
  margin-right: -1.5rem !important;
}.sdk .-mt-6 {
  margin-top: -1.5rem !important;
}.sdk .mb-0 {
  margin-bottom: 0px !important;
}.sdk .mb-1 {
  margin-bottom: 0.25rem !important;
}.sdk .mb-14 {
  margin-bottom: 3.5rem !important;
}.sdk .mb-2 {
  margin-bottom: 0.5rem !important;
}.sdk .mb-3 {
  margin-bottom: 0.75rem !important;
}.sdk .mb-4 {
  margin-bottom: 1rem !important;
}.sdk .mb-6 {
  margin-bottom: 1.5rem !important;
}.sdk .mb-8 {
  margin-bottom: 2rem !important;
}.sdk .ml-0 {
  margin-left: 0px !important;
}.sdk .ml-0\.5 {
  margin-left: 0.125rem !important;
}.sdk .ml-1 {
  margin-left: 0.25rem !important;
}.sdk .ml-2 {
  margin-left: 0.5rem !important;
}.sdk .ml-3 {
  margin-left: 0.75rem !important;
}.sdk .ml-4 {
  margin-left: 1rem !important;
}.sdk .ml-6 {
  margin-left: 1.5rem !important;
}.sdk .ml-auto {
  margin-left: auto !important;
}.sdk .mr-1 {
  margin-right: 0.25rem !important;
}.sdk .mr-2 {
  margin-right: 0.5rem !important;
}.sdk .mr-3 {
  margin-right: 0.75rem !important;
}.sdk .mr-4 {
  margin-right: 1rem !important;
}.sdk .mr-auto {
  margin-right: auto !important;
}.sdk .mt-0 {
  margin-top: 0px !important;
}.sdk .mt-0\.5 {
  margin-top: 0.125rem !important;
}.sdk .mt-1 {
  margin-top: 0.25rem !important;
}.sdk .mt-1\.5 {
  margin-top: 0.375rem !important;
}.sdk .mt-12 {
  margin-top: 3rem !important;
}.sdk .mt-2 {
  margin-top: 0.5rem !important;
}.sdk .mt-24 {
  margin-top: 6rem !important;
}.sdk .mt-3 {
  margin-top: 0.75rem !important;
}.sdk .mt-4 {
  margin-top: 1rem !important;
}.sdk .mt-5 {
  margin-top: 1.25rem !important;
}.sdk .mt-6 {
  margin-top: 1.5rem !important;
}.sdk .mt-8 {
  margin-top: 2rem !important;
}.sdk .mt-\[2px\] {
  margin-top: 2px !important;
}.sdk .mt-auto {
  margin-top: auto !important;
}.sdk .line-clamp-2 {
  overflow: hidden !important;
  display: -webkit-box !important;
  -webkit-box-orient: vertical !important;
  -webkit-line-clamp: 2 !important;
}.sdk .\!block {
  display: block !important;
}.sdk .block {
  display: block !important;
}.sdk .inline-block {
  display: inline-block !important;
}.sdk .inline {
  display: inline !important;
}.sdk .flex {
  display: flex !important;
}.sdk .inline-flex {
  display: inline-flex !important;
}.sdk .table {
  display: table !important;
}.sdk .grid {
  display: grid !important;
}.sdk .hidden {
  display: none !important;
}.sdk .aspect-square {
  aspect-ratio: 1 / 1 !important;
}.sdk .\!h-10 {
  height: 2.5rem !important;
}.sdk .h-1 {
  height: 0.25rem !important;
}.sdk .h-1\.5 {
  height: 0.375rem !important;
}.sdk .h-1\/2 {
  height: 50% !important;
}.sdk .h-1\/4 {
  height: 25% !important;
}.sdk .h-1\/5 {
  height: 20% !important;
}.sdk .h-1\/6 {
  height: 16.666667% !important;
}.sdk .h-10 {
  height: 2.5rem !important;
}.sdk .h-11 {
  height: 2.75rem !important;
}.sdk .h-12 {
  height: 3rem !important;
}.sdk .h-16 {
  height: 4rem !important;
}.sdk .h-2 {
  height: 0.5rem !important;
}.sdk .h-2\.5 {
  height: 0.625rem !important;
}.sdk .h-2\/3 {
  height: 66.666667% !important;
}.sdk .h-2\/4 {
  height: 50% !important;
}.sdk .h-2\/5 {
  height: 40% !important;
}.sdk .h-2\/6 {
  height: 33.333333% !important;
}.sdk .h-20 {
  height: 5rem !important;
}.sdk .h-24 {
  height: 6rem !important;
}.sdk .h-3 {
  height: 0.75rem !important;
}.sdk .h-3\.5 {
  height: 0.875rem !important;
}.sdk .h-3\/4 {
  height: 75% !important;
}.sdk .h-3\/5 {
  height: 60% !important;
}.sdk .h-32 {
  height: 8rem !important;
}.sdk .h-4 {
  height: 1rem !important;
}.sdk .h-4\/5 {
  height: 80% !important;
}.sdk .h-40 {
  height: 10rem !important;
}.sdk .h-48 {
  height: 12rem !important;
}.sdk .h-5 {
  height: 1.25rem !important;
}.sdk .h-5\/6 {
  height: 83.333333% !important;
}.sdk .h-6 {
  height: 1.5rem !important;
}.sdk .h-60 {
  height: 15rem !important;
}.sdk .h-64 {
  height: 16rem !important;
}.sdk .h-7 {
  height: 1.75rem !important;
}.sdk .h-8 {
  height: 2rem !important;
}.sdk .h-9 {
  height: 2.25rem !important;
}.sdk .h-\[1px\] {
  height: 1px !important;
}.sdk .h-\[200px\] {
  height: 200px !important;
}.sdk .h-\[60vh\] {
  height: 60vh !important;
}.sdk .h-\[72px\] {
  height: 72px !important;
}.sdk .h-\[calc\(100vh-40px-72px\)\] {
  height: calc(100vh - 40px - 72px) !important;
}.sdk .h-\[calc\(100vh-78px\)\] {
  height: calc(100vh - 78px) !important;
}.sdk .h-\[var\(--radix-navigation-menu-viewport-height\)\] {
  height: var(--radix-navigation-menu-viewport-height) !important;
}.sdk .h-\[var\(--radix-select-trigger-height\)\] {
  height: var(--radix-select-trigger-height) !important;
}.sdk .h-auto {
  height: auto !important;
}.sdk .h-dvh {
  height: 100dvh !important;
}.sdk .h-fit {
  height: -moz-fit-content !important;
  height: fit-content !important;
}.sdk .h-full {
  height: 100% !important;
}.sdk .h-min {
  height: -moz-min-content !important;
  height: min-content !important;
}.sdk .h-px {
  height: 1px !important;
}.sdk .h-screen {
  height: 100vh !important;
}.sdk .\!max-h-40 {
  max-height: 10rem !important;
}.sdk .max-h-32 {
  max-height: 8rem !important;
}.sdk .max-h-40 {
  max-height: 10rem !important;
}.sdk .max-h-64 {
  max-height: 16rem !important;
}.sdk .max-h-7 {
  max-height: 1.75rem !important;
}.sdk .max-h-96 {
  max-height: 24rem !important;
}.sdk .max-h-\[300px\] {
  max-height: 300px !important;
}.sdk .max-h-\[40vh\] {
  max-height: 40vh !important;
}.sdk .max-h-\[calc\(100vh-40px\)\] {
  max-height: calc(100vh - 40px) !important;
}.sdk .max-h-full {
  max-height: 100% !important;
}.sdk .max-h-screen {
  max-height: 100vh !important;
}.sdk .min-h-6 {
  min-height: 1.5rem !important;
}.sdk .min-h-\[122px\] {
  min-height: 122px !important;
}.sdk .min-h-\[4\.5rem\] {
  min-height: 4.5rem !important;
}.sdk .min-h-\[80px\] {
  min-height: 80px !important;
}.sdk .min-h-screen {
  min-height: 100vh !important;
}.sdk .\!w-24 {
  width: 6rem !important;
}.sdk .\!w-40 {
  width: 10rem !important;
}.sdk .\!w-full {
  width: 100% !important;
}.sdk .w-1\/12 {
  width: 8.333333% !important;
}.sdk .w-1\/2 {
  width: 50% !important;
}.sdk .w-1\/5 {
  width: 20% !important;
}.sdk .w-1\/6 {
  width: 16.666667% !important;
}.sdk .w-10 {
  width: 2.5rem !important;
}.sdk .w-11 {
  width: 2.75rem !important;
}.sdk .w-12 {
  width: 3rem !important;
}.sdk .w-2 {
  width: 0.5rem !important;
}.sdk .w-2\.5 {
  width: 0.625rem !important;
}.sdk .w-2\/3 {
  width: 66.666667% !important;
}.sdk .w-2\/5 {
  width: 40% !important;
}.sdk .w-24 {
  width: 6rem !important;
}.sdk .w-3 {
  width: 0.75rem !important;
}.sdk .w-3\.5 {
  width: 0.875rem !important;
}.sdk .w-3\/4 {
  width: 75% !important;
}.sdk .w-3\/5 {
  width: 60% !important;
}.sdk .w-32 {
  width: 8rem !important;
}.sdk .w-4 {
  width: 1rem !important;
}.sdk .w-4\/5 {
  width: 80% !important;
}.sdk .w-5 {
  width: 1.25rem !important;
}.sdk .w-6 {
  width: 1.5rem !important;
}.sdk .w-60 {
  width: 15rem !important;
}.sdk .w-64 {
  width: 16rem !important;
}.sdk .w-7 {
  width: 1.75rem !important;
}.sdk .w-72 {
  width: 18rem !important;
}.sdk .w-8 {
  width: 2rem !important;
}.sdk .w-80 {
  width: 20rem !important;
}.sdk .w-9 {
  width: 2.25rem !important;
}.sdk .w-\[--radix-popover-trigger-width\] {
  width: var(--radix-popover-trigger-width) !important;
}.sdk .w-\[100px\] {
  width: 100px !important;
}.sdk .w-\[1px\] {
  width: 1px !important;
}.sdk .w-\[200px\] {
  width: 200px !important;
}.sdk .w-\[300px\] {
  width: 300px !important;
}.sdk .w-\[320px\] {
  width: 320px !important;
}.sdk .w-\[72px\] {
  width: 72px !important;
}.sdk .w-\[80\%\] {
  width: 80% !important;
}.sdk .w-\[80vw\] {
  width: 80vw !important;
}.sdk .w-\[90vw\] {
  width: 90vw !important;
}.sdk .w-\[calc\(100vw-3rem\)\] {
  width: calc(100vw - 3rem) !important;
}.sdk .w-auto {
  width: auto !important;
}.sdk .w-fit {
  width: -moz-fit-content !important;
  width: fit-content !important;
}.sdk .w-full {
  width: 100% !important;
}.sdk .w-max {
  width: -moz-max-content !important;
  width: max-content !important;
}.sdk .w-min {
  width: -moz-min-content !important;
  width: min-content !important;
}.sdk .w-px {
  width: 1px !important;
}.sdk .w-screen {
  width: 100vw !important;
}.sdk .min-w-5 {
  min-width: 1.25rem !important;
}.sdk .min-w-6 {
  min-width: 1.5rem !important;
}.sdk .min-w-\[12rem\] {
  min-width: 12rem !important;
}.sdk .min-w-\[24px\] {
  min-width: 24px !important;
}.sdk .min-w-\[38px\] {
  min-width: 38px !important;
}.sdk .min-w-\[8rem\] {
  min-width: 8rem !important;
}.sdk .min-w-\[var\(--radix-select-trigger-width\)\] {
  min-width: var(--radix-select-trigger-width) !important;
}.sdk .min-w-fit {
  min-width: -moz-fit-content !important;
  min-width: fit-content !important;
}.sdk .min-w-full {
  min-width: 100% !important;
}.sdk .min-w-min {
  min-width: -moz-min-content !important;
  min-width: min-content !important;
}.sdk .\!max-w-40 {
  max-width: 10rem !important;
}.sdk .max-w-24 {
  max-width: 6rem !important;
}.sdk .max-w-\[100vw\] {
  max-width: 100vw !important;
}.sdk .max-w-\[400px\] {
  max-width: 400px !important;
}.sdk .max-w-\[620px\] {
  max-width: 620px !important;
}.sdk .max-w-\[80vw\] {
  max-width: 80vw !important;
}.sdk .max-w-\[90vw\] {
  max-width: 90vw !important;
}.sdk .max-w-\[initial\] {
  max-width: initial !important;
}.sdk .max-w-full {
  max-width: 100% !important;
}.sdk .max-w-lg {
  max-width: 32rem !important;
}.sdk .max-w-max {
  max-width: -moz-max-content !important;
  max-width: max-content !important;
}.sdk .max-w-screen-2xl {
  max-width: 1400px !important;
}.sdk .max-w-screen-sm {
  max-width: 640px !important;
}.sdk .max-w-screen-xl {
  max-width: 1280px !important;
}.sdk .max-w-screen-xs {
  max-width: 480px !important;
}.sdk .max-w-sm {
  max-width: 24rem !important;
}.sdk .\!flex-1 {
  flex: 1 1 0% !important;
}.sdk .flex-1 {
  flex: 1 1 0% !important;
}.sdk .flex-\[1\.1\] {
  flex: 1.1 !important;
}.sdk .flex-\[1\] {
  flex: 1 !important;
}.sdk .flex-\[2\] {
  flex: 2 !important;
}.sdk .shrink-0 {
  flex-shrink: 0 !important;
}.sdk .grow {
  flex-grow: 1 !important;
}.sdk .caption-bottom {
  caption-side: bottom !important;
}.sdk .border-collapse {
  border-collapse: collapse !important;
}.sdk .-translate-x-1\/2 {
  --tw-translate-x: -50% !important;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y)) !important;
}.sdk .-translate-y-1\/2 {
  --tw-translate-y: -50% !important;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y)) !important;
}.sdk .translate-x-1\/2 {
  --tw-translate-x: 50% !important;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y)) !important;
}.sdk .translate-x-\[-50\%\] {
  --tw-translate-x: -50% !important;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y)) !important;
}.sdk .translate-y-\[-50\%\] {
  --tw-translate-y: -50% !important;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y)) !important;
}.sdk .rotate-0 {
  --tw-rotate: 0deg !important;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y)) !important;
}.sdk .rotate-180 {
  --tw-rotate: 180deg !important;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y)) !important;
}.sdk .rotate-45 {
  --tw-rotate: 45deg !important;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y)) !important;
}.sdk .scale-75 {
  --tw-scale-x: .75 !important;
  --tw-scale-y: .75 !important;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y)) !important;
}.sdk .transform {
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y)) !important;
}@keyframes pulse {50% {
    opacity: .5;
  }
}.sdk .animate-pulse {
  animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite !important;
}@keyframes spin {to {
    transform: rotate(360deg);
  }
}.sdk .animate-spin {
  animation: spin 1s linear infinite !important;
}.sdk .cursor-default {
  cursor: default !important;
}.sdk .cursor-not-allowed {
  cursor: not-allowed !important;
}.sdk .cursor-pointer {
  cursor: pointer !important;
}.sdk .touch-none {
  touch-action: none !important;
}.sdk .select-none {
  -webkit-user-select: none !important;
     -moz-user-select: none !important;
          user-select: none !important;
}.sdk .resize {
  resize: both !important;
}.sdk .list-disc {
  list-style-type: disc !important;
}.sdk .list-none {
  list-style-type: none !important;
}.sdk .grid-cols-1 {
  grid-template-columns: repeat(1, minmax(0, 1fr)) !important;
}.sdk .grid-cols-12 {
  grid-template-columns: repeat(12, minmax(0, 1fr)) !important;
}.sdk .grid-cols-2 {
  grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
}.sdk .grid-cols-3 {
  grid-template-columns: repeat(3, minmax(0, 1fr)) !important;
}.sdk .grid-rows-\[0fr\] {
  grid-template-rows: 0fr !important;
}.sdk .grid-rows-\[1fr\] {
  grid-template-rows: 1fr !important;
}.sdk .flex-row {
  flex-direction: row !important;
}.sdk .flex-row-reverse {
  flex-direction: row-reverse !important;
}.sdk .flex-col {
  flex-direction: column !important;
}.sdk .flex-col-reverse {
  flex-direction: column-reverse !important;
}.sdk .flex-wrap {
  flex-wrap: wrap !important;
}.sdk .items-start {
  align-items: flex-start !important;
}.sdk .items-end {
  align-items: flex-end !important;
}.sdk .items-center {
  align-items: center !important;
}.sdk .justify-start {
  justify-content: flex-start !important;
}.sdk .justify-end {
  justify-content: flex-end !important;
}.sdk .justify-center {
  justify-content: center !important;
}.sdk .justify-between {
  justify-content: space-between !important;
}.sdk .justify-around {
  justify-content: space-around !important;
}.sdk .gap-0 {
  gap: 0px !important;
}.sdk .gap-0\.5 {
  gap: 0.125rem !important;
}.sdk .gap-1 {
  gap: 0.25rem !important;
}.sdk .gap-1\.5 {
  gap: 0.375rem !important;
}.sdk .gap-12 {
  gap: 3rem !important;
}.sdk .gap-2 {
  gap: 0.5rem !important;
}.sdk .gap-3 {
  gap: 0.75rem !important;
}.sdk .gap-3\.5 {
  gap: 0.875rem !important;
}.sdk .gap-4 {
  gap: 1rem !important;
}.sdk .gap-5 {
  gap: 1.25rem !important;
}.sdk .gap-6 {
  gap: 1.5rem !important;
}.sdk .gap-8 {
  gap: 2rem !important;
}.sdk .gap-\[18px\] {
  gap: 18px !important;
}.sdk .space-x-1 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0 !important;
  margin-right: calc(0.25rem * var(--tw-space-x-reverse)) !important;
  margin-left: calc(0.25rem * calc(1 - var(--tw-space-x-reverse))) !important;
}.sdk .space-x-2 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0 !important;
  margin-right: calc(0.5rem * var(--tw-space-x-reverse)) !important;
  margin-left: calc(0.5rem * calc(1 - var(--tw-space-x-reverse))) !important;
}.sdk .space-x-4 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0 !important;
  margin-right: calc(1rem * var(--tw-space-x-reverse)) !important;
  margin-left: calc(1rem * calc(1 - var(--tw-space-x-reverse))) !important;
}.sdk .space-y-0 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0 !important;
  margin-top: calc(0px * calc(1 - var(--tw-space-y-reverse))) !important;
  margin-bottom: calc(0px * var(--tw-space-y-reverse)) !important;
}.sdk .space-y-1 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0 !important;
  margin-top: calc(0.25rem * calc(1 - var(--tw-space-y-reverse))) !important;
  margin-bottom: calc(0.25rem * var(--tw-space-y-reverse)) !important;
}.sdk .space-y-1\.5 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0 !important;
  margin-top: calc(0.375rem * calc(1 - var(--tw-space-y-reverse))) !important;
  margin-bottom: calc(0.375rem * var(--tw-space-y-reverse)) !important;
}.sdk .space-y-10 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0 !important;
  margin-top: calc(2.5rem * calc(1 - var(--tw-space-y-reverse))) !important;
  margin-bottom: calc(2.5rem * var(--tw-space-y-reverse)) !important;
}.sdk .space-y-2 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0 !important;
  margin-top: calc(0.5rem * calc(1 - var(--tw-space-y-reverse))) !important;
  margin-bottom: calc(0.5rem * var(--tw-space-y-reverse)) !important;
}.sdk .space-y-4 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0 !important;
  margin-top: calc(1rem * calc(1 - var(--tw-space-y-reverse))) !important;
  margin-bottom: calc(1rem * var(--tw-space-y-reverse)) !important;
}.sdk .space-y-5 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0 !important;
  margin-top: calc(1.25rem * calc(1 - var(--tw-space-y-reverse))) !important;
  margin-bottom: calc(1.25rem * var(--tw-space-y-reverse)) !important;
}.sdk .space-y-6 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0 !important;
  margin-top: calc(1.5rem * calc(1 - var(--tw-space-y-reverse))) !important;
  margin-bottom: calc(1.5rem * var(--tw-space-y-reverse)) !important;
}.sdk .self-start {
  align-self: flex-start !important;
}.sdk .self-end {
  align-self: flex-end !important;
}.sdk .self-center {
  align-self: center !important;
}.sdk .self-stretch {
  align-self: stretch !important;
}.sdk .overflow-auto {
  overflow: auto !important;
}.sdk .overflow-hidden {
  overflow: hidden !important;
}.sdk .overflow-clip {
  overflow: clip !important;
}.sdk .overflow-x-auto {
  overflow-x: auto !important;
}.sdk .overflow-y-auto {
  overflow-y: auto !important;
}.sdk .overflow-x-hidden {
  overflow-x: hidden !important;
}.sdk .overscroll-y-contain {
  overscroll-behavior-y: contain !important;
}.sdk .text-ellipsis {
  text-overflow: ellipsis !important;
}.sdk .whitespace-nowrap {
  white-space: nowrap !important;
}.sdk .whitespace-pre-wrap {
  white-space: pre-wrap !important;
}.sdk .text-wrap {
  text-wrap: wrap !important;
}.sdk .text-nowrap {
  text-wrap: nowrap !important;
}.sdk .break-words {
  overflow-wrap: break-word !important;
}.sdk .rounded-2xl {
  border-radius: 1rem !important;
}.sdk .rounded-\[inherit\] {
  border-radius: inherit !important;
}.sdk .rounded-full {
  border-radius: 9999px !important;
}.sdk .rounded-lg {
  border-radius: var(--radius) !important;
}.sdk .rounded-md {
  border-radius: calc(var(--radius) - 2px) !important;
}.sdk .rounded-none {
  border-radius: 0px !important;
}.sdk .rounded-sm {
  border-radius: calc(var(--radius) - 4px) !important;
}.sdk .rounded-xl {
  border-radius: 0.75rem !important;
}.sdk .\!rounded-l-lg {
  border-top-left-radius: var(--radius) !important;
  border-bottom-left-radius: var(--radius) !important;
}.sdk .\!rounded-r-lg {
  border-top-right-radius: var(--radius) !important;
  border-bottom-right-radius: var(--radius) !important;
}.sdk .rounded-b-none {
  border-bottom-right-radius: 0px !important;
  border-bottom-left-radius: 0px !important;
}.sdk .rounded-l-none {
  border-top-left-radius: 0px !important;
  border-bottom-left-radius: 0px !important;
}.sdk .rounded-r-none {
  border-top-right-radius: 0px !important;
  border-bottom-right-radius: 0px !important;
}.sdk .rounded-t-\[10px\] {
  border-top-left-radius: 10px !important;
  border-top-right-radius: 10px !important;
}.sdk .rounded-t-none {
  border-top-left-radius: 0px !important;
  border-top-right-radius: 0px !important;
}.sdk .rounded-t-sm {
  border-top-left-radius: calc(var(--radius) - 4px) !important;
  border-top-right-radius: calc(var(--radius) - 4px) !important;
}.sdk .rounded-tl-sm {
  border-top-left-radius: calc(var(--radius) - 4px) !important;
}.sdk .\!border {
  border-width: 1px !important;
}.sdk .border {
  border-width: 1px !important;
}.sdk .border-0 {
  border-width: 0px !important;
}.sdk .border-2 {
  border-width: 2px !important;
}.sdk .border-b {
  border-bottom-width: 1px !important;
}.sdk .border-b-0 {
  border-bottom-width: 0px !important;
}.sdk .border-b-2 {
  border-bottom-width: 2px !important;
}.sdk .border-l {
  border-left-width: 1px !important;
}.sdk .border-l-0 {
  border-left-width: 0px !important;
}.sdk .border-r {
  border-right-width: 1px !important;
}.sdk .border-t {
  border-top-width: 1px !important;
}.sdk .border-t-0 {
  border-top-width: 0px !important;
}.sdk .border-none {
  border-style: none !important;
}.sdk .\!border-border {
  border-color: hsl(var(--border)) !important;
}.sdk .border-\[rgb\(2\2c 157\2c 224\)\] {
  --tw-border-opacity: 1 !important;
  border-color: rgb(2 157 224 / var(--tw-border-opacity)) !important;
}.sdk .border-border {
  border-color: hsl(var(--border)) !important;
}.sdk .border-border-error {
  border-color: hsl(var(--border-error)) !important;
}.sdk .border-border-secondary {
  border-color: hsl(var(--border-secondary)) !important;
}.sdk .border-destructive {
  border-color: hsl(var(--destructive)) !important;
}.sdk .border-destructive\/50 {
  border-color: hsl(var(--destructive) / 0.5) !important;
}.sdk .border-input {
  border-color: hsl(var(--input)) !important;
}.sdk .border-primary {
  border-color: rgb(var(--primary)) !important;
}.sdk .border-primary\/20 {
  border-color: rgb(var(--primary) / 0.2) !important;
}.sdk .border-ring {
  border-color: hsl(var(--ring)) !important;
}.sdk .border-success {
  border-color: hsla(var(--success)) !important;
}.sdk .border-transparent {
  border-color: transparent !important;
}.sdk .border-white {
  --tw-border-opacity: 1 !important;
  border-color: rgb(255 255 255 / var(--tw-border-opacity)) !important;
}.sdk .border-b-border-secondary {
  border-bottom-color: hsl(var(--border-secondary)) !important;
}.sdk .border-b-primary\/20 {
  border-bottom-color: rgb(var(--primary) / 0.2) !important;
}.sdk .border-b-transparent {
  border-bottom-color: transparent !important;
}.sdk .border-l-transparent {
  border-left-color: transparent !important;
}.sdk .border-t-primary\/20 {
  border-top-color: rgb(var(--primary) / 0.2) !important;
}.sdk .border-t-transparent {
  border-top-color: transparent !important;
}.sdk .\!bg-background {
  background-color: hsl(var(--background)) !important;
}.sdk .\!bg-card {
  background-color: hsl(var(--card)) !important;
}.sdk .bg-\[\#EAECF0\] {
  --tw-bg-opacity: 1 !important;
  background-color: rgb(234 236 240 / var(--tw-bg-opacity)) !important;
}.sdk .bg-\[rgba\(38\2c 38\2c 38\2c \.03\)\] {
  background-color: rgba(38,38,38,.03) !important;
}.sdk .bg-accent {
  background-color: hsl(var(--accent)) !important;
}.sdk .bg-accent-foreground {
  background-color: hsl(var(--accent-foreground)) !important;
}.sdk .bg-background {
  background-color: hsl(var(--background)) !important;
}.sdk .bg-background-quaternary {
  background-color: hsl(var(--background-quaternary)) !important;
}.sdk .bg-background-secondary {
  background-color: hsla(var(--background-secondary)) !important;
}.sdk .bg-background-tertiary {
  background-color: hsl(var(--background-tertiary)) !important;
}.sdk .bg-background\/10 {
  background-color: hsl(var(--background) / 0.1) !important;
}.sdk .bg-background\/70 {
  background-color: hsl(var(--background) / 0.7) !important;
}.sdk .bg-black\/80 {
  background-color: rgb(0 0 0 / 0.8) !important;
}.sdk .bg-border {
  background-color: hsl(var(--border)) !important;
}.sdk .bg-border-secondary {
  background-color: hsl(var(--border-secondary)) !important;
}.sdk .bg-card {
  background-color: hsl(var(--card)) !important;
}.sdk .bg-destructive {
  background-color: hsl(var(--destructive)) !important;
}.sdk .bg-destructive\/10 {
  background-color: hsl(var(--destructive) / 0.1) !important;
}.sdk .bg-destructive\/20 {
  background-color: hsl(var(--destructive) / 0.2) !important;
}.sdk .bg-destructive\/90 {
  background-color: hsl(var(--destructive) / 0.9) !important;
}.sdk .bg-gray-300 {
  --tw-bg-opacity: 1 !important;
  background-color: rgb(209 213 219 / var(--tw-bg-opacity)) !important;
}.sdk .bg-muted {
  background-color: hsl(var(--muted)) !important;
}.sdk .bg-muted\/50 {
  background-color: hsl(var(--muted) / 0.5) !important;
}.sdk .bg-popover {
  background-color: hsl(var(--popover)) !important;
}.sdk .bg-primary {
  background-color: rgb(var(--primary)) !important;
}.sdk .bg-primary\/10 {
  background-color: rgb(var(--primary) / 0.1) !important;
}.sdk .bg-primary\/20 {
  background-color: rgb(var(--primary) / 0.2) !important;
}.sdk .bg-secondary {
  background-color: rgb(var(--secondary)) !important;
}.sdk .bg-secondary\/80 {
  background-color: rgb(var(--secondary) / 0.8) !important;
}.sdk .bg-success {
  background-color: hsla(var(--success)) !important;
}.sdk .bg-success\/10 {
  background-color: hsla(var(--success), 0.1) !important;
}.sdk .bg-success\/5 {
  background-color: hsla(var(--success), 0.05) !important;
}.sdk .bg-transparent {
  background-color: transparent !important;
}.sdk .bg-opacity-10 {
  --tw-bg-opacity: 0.1 !important;
}.sdk .bg-gradient-to-r {
  background-image: linear-gradient(to right, var(--tw-gradient-stops)) !important;
}.sdk .from-gradient-start {
  --tw-gradient-from: hsl(var(--gradient-start)) var(--tw-gradient-from-position) !important;
  --tw-gradient-to: hsl(var(--gradient-start) / 0) var(--tw-gradient-to-position) !important;
  --tw-gradient-stops: var(--tw-gradient-from), var(--tw-gradient-to) !important;
}.sdk .to-gradient-stop {
  --tw-gradient-to: hsl(var(--gradient-stop)) var(--tw-gradient-to-position) !important;
}.sdk .bg-clip-text {
  -webkit-background-clip: text !important;
          background-clip: text !important;
}.sdk .bg-center {
  background-position: center !important;
}.sdk .fill-\[\#0A66C2\] {
  fill: #0A66C2 !important;
}.sdk .fill-\[\#1877F2\] {
  fill: #1877F2 !important;
}.sdk .fill-current {
  fill: currentColor !important;
}.sdk .fill-muted {
  fill: hsl(var(--muted)) !important;
}.sdk .stroke-current {
  stroke: currentColor !important;
}.sdk .stroke-destructive {
  stroke: hsl(var(--destructive)) !important;
}.sdk .stroke-foreground {
  stroke: hsl(var(--foreground)) !important;
}.sdk .stroke-muted {
  stroke: hsl(var(--muted)) !important;
}.sdk .stroke-muted-foreground {
  stroke: hsl(var(--muted-foreground)) !important;
}.sdk .stroke-popover-foreground {
  stroke: hsl(var(--popover-foreground)) !important;
}.sdk .stroke-success {
  stroke: hsla(var(--success)) !important;
}.sdk .stroke-2 {
  stroke-width: 2 !important;
}.sdk .object-contain {
  -o-object-fit: contain !important;
     object-fit: contain !important;
}.sdk .object-cover {
  -o-object-fit: cover !important;
     object-fit: cover !important;
}.sdk .object-fill {
  -o-object-fit: fill !important;
     object-fit: fill !important;
}.sdk .p-0 {
  padding: 0px !important;
}.sdk .p-1 {
  padding: 0.25rem !important;
}.sdk .p-10 {
  padding: 2.5rem !important;
}.sdk .p-2 {
  padding: 0.5rem !important;
}.sdk .p-2\.5 {
  padding: 0.625rem !important;
}.sdk .p-3 {
  padding: 0.75rem !important;
}.sdk .p-4 {
  padding: 1rem !important;
}.sdk .p-5 {
  padding: 1.25rem !important;
}.sdk .p-6 {
  padding: 1.5rem !important;
}.sdk .p-8 {
  padding: 2rem !important;
}.sdk .p-9 {
  padding: 2.25rem !important;
}.sdk .p-\[1px\] {
  padding: 1px !important;
}.sdk .\!px-2 {
  padding-left: 0.5rem !important;
  padding-right: 0.5rem !important;
}.sdk .\!px-3 {
  padding-left: 0.75rem !important;
  padding-right: 0.75rem !important;
}.sdk .\!py-1 {
  padding-top: 0.25rem !important;
  padding-bottom: 0.25rem !important;
}.sdk .\!py-2 {
  padding-top: 0.5rem !important;
  padding-bottom: 0.5rem !important;
}.sdk .px-0 {
  padding-left: 0px !important;
  padding-right: 0px !important;
}.sdk .px-1 {
  padding-left: 0.25rem !important;
  padding-right: 0.25rem !important;
}.sdk .px-12 {
  padding-left: 3rem !important;
  padding-right: 3rem !important;
}.sdk .px-2 {
  padding-left: 0.5rem !important;
  padding-right: 0.5rem !important;
}.sdk .px-2\.5 {
  padding-left: 0.625rem !important;
  padding-right: 0.625rem !important;
}.sdk .px-3 {
  padding-left: 0.75rem !important;
  padding-right: 0.75rem !important;
}.sdk .px-4 {
  padding-left: 1rem !important;
  padding-right: 1rem !important;
}.sdk .px-5 {
  padding-left: 1.25rem !important;
  padding-right: 1.25rem !important;
}.sdk .px-6 {
  padding-left: 1.5rem !important;
  padding-right: 1.5rem !important;
}.sdk .px-8 {
  padding-left: 2rem !important;
  padding-right: 2rem !important;
}.sdk .py-0 {
  padding-top: 0px !important;
  padding-bottom: 0px !important;
}.sdk .py-0\.5 {
  padding-top: 0.125rem !important;
  padding-bottom: 0.125rem !important;
}.sdk .py-1 {
  padding-top: 0.25rem !important;
  padding-bottom: 0.25rem !important;
}.sdk .py-1\.5 {
  padding-top: 0.375rem !important;
  padding-bottom: 0.375rem !important;
}.sdk .py-2 {
  padding-top: 0.5rem !important;
  padding-bottom: 0.5rem !important;
}.sdk .py-3 {
  padding-top: 0.75rem !important;
  padding-bottom: 0.75rem !important;
}.sdk .py-4 {
  padding-top: 1rem !important;
  padding-bottom: 1rem !important;
}.sdk .py-6 {
  padding-top: 1.5rem !important;
  padding-bottom: 1.5rem !important;
}.sdk .py-8 {
  padding-top: 2rem !important;
  padding-bottom: 2rem !important;
}.sdk .pb-0 {
  padding-bottom: 0px !important;
}.sdk .pb-12 {
  padding-bottom: 3rem !important;
}.sdk .pb-2 {
  padding-bottom: 0.5rem !important;
}.sdk .pb-3 {
  padding-bottom: 0.75rem !important;
}.sdk .pb-4 {
  padding-bottom: 1rem !important;
}.sdk .pb-5 {
  padding-bottom: 1.25rem !important;
}.sdk .pb-6 {
  padding-bottom: 1.5rem !important;
}.sdk .pb-8 {
  padding-bottom: 2rem !important;
}.sdk .pb-\[100\%\] {
  padding-bottom: 100% !important;
}.sdk .pl-0 {
  padding-left: 0px !important;
}.sdk .pl-10 {
  padding-left: 2.5rem !important;
}.sdk .pl-2 {
  padding-left: 0.5rem !important;
}.sdk .pl-2\.5 {
  padding-left: 0.625rem !important;
}.sdk .pl-3 {
  padding-left: 0.75rem !important;
}.sdk .pl-8 {
  padding-left: 2rem !important;
}.sdk .pr-10 {
  padding-right: 2.5rem !important;
}.sdk .pr-2 {
  padding-right: 0.5rem !important;
}.sdk .pr-2\.5 {
  padding-right: 0.625rem !important;
}.sdk .pr-3 {
  padding-right: 0.75rem !important;
}.sdk .pr-4 {
  padding-right: 1rem !important;
}.sdk .pr-6 {
  padding-right: 1.5rem !important;
}.sdk .pr-8 {
  padding-right: 2rem !important;
}.sdk .pt-0 {
  padding-top: 0px !important;
}.sdk .pt-1 {
  padding-top: 0.25rem !important;
}.sdk .pt-12 {
  padding-top: 3rem !important;
}.sdk .pt-3 {
  padding-top: 0.75rem !important;
}.sdk .pt-4 {
  padding-top: 1rem !important;
}.sdk .pt-6 {
  padding-top: 1.5rem !important;
}.sdk .pt-8 {
  padding-top: 2rem !important;
}.sdk .pt-\[56\.25\%\] {
  padding-top: 56.25% !important;
}.sdk .text-left {
  text-align: left !important;
}.sdk .text-center {
  text-align: center !important;
}.sdk .text-right {
  text-align: right !important;
}.sdk .text-start {
  text-align: start !important;
}.sdk .align-middle {
  vertical-align: middle !important;
}.sdk .\!text-sm {
  font-size: 0.875rem !important;
  line-height: 1.25rem !important;
}.sdk .text-2xl {
  font-size: 1.5rem !important;
  line-height: 2rem !important;
}.sdk .text-3xl {
  font-size: 1.875rem !important;
  line-height: 2.25rem !important;
}.sdk .text-4xl {
  font-size: 2.25rem !important;
  line-height: 2.5rem !important;
}.sdk .text-5xl {
  font-size: 3rem !important;
  line-height: 1 !important;
}.sdk .text-\[0\.8rem\] {
  font-size: 0.8rem !important;
}.sdk .text-\[10px\] {
  font-size: 10px !important;
}.sdk .text-\[7rem\] {
  font-size: 7rem !important;
}.sdk .text-base {
  font-size: 1rem !important;
  line-height: 1.5rem !important;
}.sdk .text-lg {
  font-size: 1.125rem !important;
  line-height: 1.75rem !important;
}.sdk .text-sm {
  font-size: 0.875rem !important;
  line-height: 1.25rem !important;
}.sdk .text-xl {
  font-size: 1.25rem !important;
  line-height: 1.75rem !important;
}.sdk .text-xs {
  font-size: 0.75rem !important;
  line-height: 1rem !important;
}.sdk .font-bold {
  font-weight: 700 !important;
}.sdk .font-light {
  font-weight: 300 !important;
}.sdk .font-medium {
  font-weight: 500 !important;
}.sdk .font-normal {
  font-weight: 400 !important;
}.sdk .font-semibold {
  font-weight: 600 !important;
}.sdk .uppercase {
  text-transform: uppercase !important;
}.sdk .lowercase {
  text-transform: lowercase !important;
}.sdk .capitalize {
  text-transform: capitalize !important;
}.sdk .\!leading-\[1\.25em\] {
  line-height: 1.25em !important;
}.sdk .leading-5 {
  line-height: 1.25rem !important;
}.sdk .leading-\[1\.25em\] {
  line-height: 1.25em !important;
}.sdk .leading-\[1\.5\] {
  line-height: 1.5 !important;
}.sdk .leading-none {
  line-height: 1 !important;
}.sdk .leading-normal {
  line-height: 1.5 !important;
}.sdk .leading-tight {
  line-height: 1.25 !important;
}.sdk .tracking-tight {
  letter-spacing: -0.025em !important;
}.sdk .tracking-widest {
  letter-spacing: 0.1em !important;
}.sdk .\!text-foreground {
  color: hsl(var(--foreground)) !important;
}.sdk .text-\[\#029DE099\] {
  color: #029DE099 !important;
}.sdk .text-\[\#F79009\] {
  --tw-text-opacity: 1 !important;
  color: rgb(247 144 9 / var(--tw-text-opacity)) !important;
}.sdk .text-\[\#FBD647\] {
  --tw-text-opacity: 1 !important;
  color: rgb(251 214 71 / var(--tw-text-opacity)) !important;
}.sdk .text-\[rgb\(2\2c 157\2c 224\)\] {
  --tw-text-opacity: 1 !important;
  color: rgb(2 157 224 / var(--tw-text-opacity)) !important;
}.sdk .text-accent {
  color: hsl(var(--accent)) !important;
}.sdk .text-accent-foreground {
  color: hsl(var(--accent-foreground)) !important;
}.sdk .text-background {
  color: hsl(var(--background)) !important;
}.sdk .text-background\/80 {
  color: hsl(var(--background) / 0.8) !important;
}.sdk .text-border-error {
  color: hsl(var(--border-error)) !important;
}.sdk .text-card-foreground {
  color: hsl(var(--card-foreground)) !important;
}.sdk .text-current {
  color: currentColor !important;
}.sdk .text-destructive {
  color: hsl(var(--destructive)) !important;
}.sdk .text-destructive-foreground {
  color: hsl(var(--destructive-foreground)) !important;
}.sdk .text-foreground {
  color: hsl(var(--foreground)) !important;
}.sdk .text-foreground\/50 {
  color: hsl(var(--foreground) / 0.5) !important;
}.sdk .text-gray-700 {
  --tw-text-opacity: 1 !important;
  color: rgb(55 65 81 / var(--tw-text-opacity)) !important;
}.sdk .text-inherit {
  color: inherit !important;
}.sdk .text-muted {
  color: hsl(var(--muted)) !important;
}.sdk .text-muted-foreground {
  color: hsl(var(--muted-foreground)) !important;
}.sdk .text-popover-foreground {
  color: hsl(var(--popover-foreground)) !important;
}.sdk .text-primary {
  color: rgb(var(--primary)) !important;
}.sdk .text-primary-foreground {
  color: hsl(var(--primary-foreground)) !important;
}.sdk .text-secondary {
  color: rgb(var(--secondary)) !important;
}.sdk .text-secondary-foreground {
  color: hsl(var(--secondary-foreground)) !important;
}.sdk .text-secondary\/70 {
  color: rgb(var(--secondary) / 0.7) !important;
}.sdk .text-success {
  color: hsla(var(--success)) !important;
}.sdk .text-tertiary {
  color: hsl(var(--tertiary)) !important;
}.sdk .text-transparent {
  color: transparent !important;
}.sdk .text-white {
  --tw-text-opacity: 1 !important;
  color: rgb(255 255 255 / var(--tw-text-opacity)) !important;
}.sdk .underline {
  text-decoration-line: underline !important;
}.sdk .underline-offset-4 {
  text-underline-offset: 4px !important;
}.sdk .opacity-0 {
  opacity: 0 !important;
}.sdk .opacity-100 {
  opacity: 1 !important;
}.sdk .opacity-50 {
  opacity: 0.5 !important;
}.sdk .opacity-60 {
  opacity: 0.6 !important;
}.sdk .opacity-70 {
  opacity: 0.7 !important;
}.sdk .opacity-90 {
  opacity: 0.9 !important;
}.sdk .shadow-lg {
  --tw-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1) !important;
  --tw-shadow-colored: 0 10px 15px -3px var(--tw-shadow-color), 0 4px 6px -4px var(--tw-shadow-color) !important;
  box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow) !important;
}.sdk .shadow-md {
  --tw-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1) !important;
  --tw-shadow-colored: 0 4px 6px -1px var(--tw-shadow-color), 0 2px 4px -2px var(--tw-shadow-color) !important;
  box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow) !important;
}.sdk .shadow-none {
  --tw-shadow: 0 0 #0000 !important;
  --tw-shadow-colored: 0 0 #0000 !important;
  box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow) !important;
}.sdk .shadow-sm {
  --tw-shadow: 0 1px 2px 0 rgb(0 0 0 / 0.05) !important;
  --tw-shadow-colored: 0 1px 2px 0 var(--tw-shadow-color) !important;
  box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow) !important;
}.sdk .shadow-xl {
  --tw-shadow: 0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1) !important;
  --tw-shadow-colored: 0 20px 25px -5px var(--tw-shadow-color), 0 8px 10px -6px var(--tw-shadow-color) !important;
  box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow) !important;
}.sdk .shadow-border {
  --tw-shadow-color: hsl(var(--border)) !important;
  --tw-shadow: var(--tw-shadow-colored) !important;
}.sdk .outline-none {
  outline: 2px solid transparent !important;
  outline-offset: 2px !important;
}.sdk .outline {
  outline-style: solid !important;
}.sdk .ring-0 {
  --tw-ring-offset-shadow: var(--tw-ring-inset) 0 0 0 var(--tw-ring-offset-width) var(--tw-ring-offset-color) !important;
  --tw-ring-shadow: var(--tw-ring-inset) 0 0 0 calc(0px + var(--tw-ring-offset-width)) var(--tw-ring-color) !important;
  box-shadow: var(--tw-ring-offset-shadow), var(--tw-ring-shadow), var(--tw-shadow, 0 0 #0000) !important;
}.sdk .ring-offset-background {
  --tw-ring-offset-color: hsl(var(--background)) !important;
}.sdk .brightness-75 {
  --tw-brightness: brightness(.75) !important;
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow) !important;
}.sdk .filter {
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow) !important;
}.sdk .transition {
  transition-property: color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, -webkit-backdrop-filter !important;
  transition-property: color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, backdrop-filter !important;
  transition-property: color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, backdrop-filter, -webkit-backdrop-filter !important;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1) !important;
  transition-duration: 150ms !important;
}.sdk .transition-\[grid-template-rows\2c _opacity\] {
  transition-property: grid-template-rows, opacity !important;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1) !important;
  transition-duration: 150ms !important;
}.sdk .transition-all {
  transition-property: all !important;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1) !important;
  transition-duration: 150ms !important;
}.sdk .transition-colors {
  transition-property: color, background-color, border-color, text-decoration-color, fill, stroke !important;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1) !important;
  transition-duration: 150ms !important;
}.sdk .transition-none {
  transition-property: none !important;
}.sdk .transition-opacity {
  transition-property: opacity !important;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1) !important;
  transition-duration: 150ms !important;
}.sdk .transition-transform {
  transition-property: transform !important;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1) !important;
  transition-duration: 150ms !important;
}.sdk .duration-200 {
  transition-duration: 200ms !important;
}.sdk .duration-300 {
  transition-duration: 300ms !important;
}.sdk .duration-500 {
  transition-duration: 500ms !important;
}.sdk .ease-in-out {
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1) !important;
}@keyframes enter {from {
    opacity: var(--tw-enter-opacity, 1);
    transform: translate3d(var(--tw-enter-translate-x, 0), var(--tw-enter-translate-y, 0), 0) scale3d(var(--tw-enter-scale, 1), var(--tw-enter-scale, 1), var(--tw-enter-scale, 1)) rotate(var(--tw-enter-rotate, 0));
  }
}@keyframes exit {to {
    opacity: var(--tw-exit-opacity, 1);
    transform: translate3d(var(--tw-exit-translate-x, 0), var(--tw-exit-translate-y, 0), 0) scale3d(var(--tw-exit-scale, 1), var(--tw-exit-scale, 1), var(--tw-exit-scale, 1)) rotate(var(--tw-exit-rotate, 0));
  }
}.sdk .animate-in {
  animation-name: enter !important;
  animation-duration: 150ms !important;
  --tw-enter-opacity: initial !important;
  --tw-enter-scale: initial !important;
  --tw-enter-rotate: initial !important;
  --tw-enter-translate-x: initial !important;
  --tw-enter-translate-y: initial !important;
}.sdk .fade-in-0 {
  --tw-enter-opacity: 0 !important;
}.sdk .fade-in-80 {
  --tw-enter-opacity: 0.8 !important;
}.sdk .zoom-in-95 {
  --tw-enter-scale: .95 !important;
}.sdk .duration-200 {
  animation-duration: 200ms !important;
}.sdk .duration-300 {
  animation-duration: 300ms !important;
}.sdk .duration-500 {
  animation-duration: 500ms !important;
}.sdk .ease-in-out {
  animation-timing-function: cubic-bezier(0.4, 0, 0.2, 1) !important;
}.sdk .paused {
  animation-play-state: paused !important;
}:root {
  --background: 0 0% 100%; /* OK */
  --background-secondary: 210, 100%, 17%; /* OK */
  --background-tertiary: 195, 50%, 97%; /* OK */
  --background-quaternary: 198, 98%, 44%, 0.1;
  --foreground: 221, 43%, 11%; /* OK */
  --card: 0 0% 100%; /* OK */
  --card-foreground: 221, 43%, 11%; /* OK */
  --popover: 0, 0%, 100%; /* OK */
  --popover-foreground: 220, 13%, 46%; /* OK */
  --primary: 2 157 224; /* OK */
  --primary-foreground: 0, 0%, 100%; /* OK */
  --secondary: 0 43 86; /* OK */
  --secondary-foreground: 220, 17%, 93%; /* OK */
  --tertiary: 216, 18%, 34%;
  --warning: 28, 97%, 44%;
  --muted: 216, 16%, 84%; /* OK */
  --muted-foreground: 215.4 16.3% 46.9%;
  --accent: 48, 96%, 63%; /* OK */
  --accent-foreground: 216, 100%, 97%; /* OK */
  --destructive: 0 84.2% 60.2%;
  --destructive-soft: 4, 88%, 97%, 1;
  --destructive-foreground: 210 40% 98%;
  --success: 152, 77%, 39%;
  --advance: 237, 77%, 59%;
  --border: 220, 17%, 93%; /* OK */
  --border-secondary: 198, 98%, 44%, 0.2; /* OK */
  --border-error: 4, 96%, 80%, 1;
  --input: 216, 16%, 84%; /* OK */
  --ring: 217, 31%, 73%;
  --radius: 0.5rem; /* OK */

  --gradient-start: 211, 83%, 39%;
  --gradient-stop: 214, 100%, 67%;
}.dark {
  --background: 216, 24%, 11%;
  --background-secondary: 215, 32%, 17%; /* OK */
  --background-tertiary: 221, 43%, 11%;
  --background-quaternary: 198, 98%, 20%, 0.1;
  --foreground: 220, 22%, 96%;
  --card: 215, 32%, 17%;
  --card-foreground: 220, 22%, 96%;
  --popover: 215, 32%, 17%;
  --popover-foreground: 220, 22%, 96%;
  --primary: 59 130 246;
  --primary-foreground: 222.2 47.4% 11.2%;
  --secondary: 149 169 223;
  --secondary-foreground: 210 40% 98%;
  --warning: 28, 97%, 44%;
  --tertiary: 215, 57%, 72%;
  --muted: 218, 15%, 65%;
  --muted-foreground: 220, 22%, 96%;
  --accent: 217.2 91.2% 72%;
  --accent-foreground: 215, 32%, 23%;
  --destructive: 0 84.2% 60.2%;
  --destructive-soft: 4, 88%, 97%, 1;
  --destructive-foreground: 210 40% 98%;
  --success: 152, 77%, 39%;
  --advance: 237, 100%, 84%;
  --border: 215, 18%, 34%;
  --border-error: 4, 96%, 80%, 1;
  --input: 217.2 32.6% 17.5%;
  --ring: 224.3 76.3% 48%;

  --gradient-start: 216, 16%, 84%;
  --gradient-stop: 216, 16%, 84%;
}.sdk {
  font-family: 'Poppins', ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont,
  'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif,
  'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol',
  'Noto Color Emoji';
}#ehub-sdk * {
  border-color: hsl(var(--border)) !important;
}#ehub-root #ehub-sdk {
  background-color: hsl(var(--background)) !important;
  color: hsl(var(--foreground)) !important;
  font-family: 'Poppins', ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, Noto Sans, sans-serif, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji !important;
  font-feature-settings: "rlig" 1, "calt" 1 !important;
}:host, html {
  -webkit-text-size-adjust: 100%  !important;
  font-feature-settings: normal  !important;
  font-variation-settings: normal  !important;
  -moz-tab-size: 4  !important;
  -o-tab-size: 4 !important;
  tab-size: 4  !important;
  -webkit-tap-highlight-color: transparent  !important;
  font-size: 16px !important;
}body {
  margin: 0  !important;
}.sdk .group {
  background: transparent !important;
}.sdk .file\:border-0::file-selector-button {
  border-width: 0px !important;
}.sdk .file\:bg-transparent::file-selector-button {
  background-color: transparent !important;
}.sdk .file\:text-sm::file-selector-button {
  font-size: 0.875rem !important;
  line-height: 1.25rem !important;
}.sdk .file\:font-medium::file-selector-button {
  font-weight: 500 !important;
}.sdk .placeholder\:text-muted-foreground::-moz-placeholder {
  color: hsl(var(--muted-foreground)) !important;
}.sdk .placeholder\:text-muted-foreground::placeholder {
  color: hsl(var(--muted-foreground)) !important;
}.sdk .after\:absolute::after {
  content: var(--tw-content) !important;
  position: absolute !important;
}.sdk .after\:inset-y-0::after {
  content: var(--tw-content) !important;
  top: 0px !important;
  bottom: 0px !important;
}.sdk .after\:left-1\/2::after {
  content: var(--tw-content) !important;
  left: 50% !important;
}.sdk .after\:w-1::after {
  content: var(--tw-content) !important;
  width: 0.25rem !important;
}.sdk .after\:-translate-x-1\/2::after {
  content: var(--tw-content) !important;
  --tw-translate-x: -50% !important;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y)) !important;
}.sdk .first\:pl-4:first-child {
  padding-left: 1rem !important;
}.sdk .last\:pr-4:last-child {
  padding-right: 1rem !important;
}.sdk .autofill\:bg-background:-webkit-autofill {
  background-color: hsl(var(--background)) !important;
}.sdk .autofill\:bg-background:autofill {
  background-color: hsl(var(--background)) !important;
}.sdk .focus-within\:relative:focus-within {
  position: relative !important;
}.sdk .focus-within\:z-20:focus-within {
  z-index: 20 !important;
}.sdk .hover\:scale-110:hover {
  --tw-scale-x: 1.1 !important;
  --tw-scale-y: 1.1 !important;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y)) !important;
}.sdk .hover\:border-primary:hover {
  border-color: rgb(var(--primary)) !important;
}.sdk .hover\:bg-\[rgb\(2\2c 157\2c 224\)\]:hover {
  --tw-bg-opacity: 1 !important;
  background-color: rgb(2 157 224 / var(--tw-bg-opacity)) !important;
}.sdk .hover\:bg-accent:hover {
  background-color: hsl(var(--accent)) !important;
}.sdk .hover\:bg-accent-foreground:hover {
  background-color: hsl(var(--accent-foreground)) !important;
}.sdk .hover\:bg-background\/20:hover {
  background-color: hsl(var(--background) / 0.2) !important;
}.sdk .hover\:bg-card:hover {
  background-color: hsl(var(--card)) !important;
}.sdk .hover\:bg-destructive:hover {
  background-color: hsl(var(--destructive)) !important;
}.sdk .hover\:bg-destructive\/80:hover {
  background-color: hsl(var(--destructive) / 0.8) !important;
}.sdk .hover\:bg-muted:hover {
  background-color: hsl(var(--muted)) !important;
}.sdk .hover\:bg-muted\/50:hover {
  background-color: hsl(var(--muted) / 0.5) !important;
}.sdk .hover\:bg-primary:hover {
  background-color: rgb(var(--primary)) !important;
}.sdk .hover\:bg-primary\/80:hover {
  background-color: rgb(var(--primary) / 0.8) !important;
}.sdk .hover\:bg-secondary:hover {
  background-color: rgb(var(--secondary)) !important;
}.sdk .hover\:bg-secondary\/80:hover {
  background-color: rgb(var(--secondary) / 0.8) !important;
}.sdk .hover\:bg-transparent:hover {
  background-color: transparent !important;
}.sdk .hover\:text-accent-foreground:hover {
  color: hsl(var(--accent-foreground)) !important;
}.sdk .hover\:text-background:hover {
  color: hsl(var(--background)) !important;
}.sdk .hover\:text-card-foreground:hover {
  color: hsl(var(--card-foreground)) !important;
}.sdk .hover\:text-foreground:hover {
  color: hsl(var(--foreground)) !important;
}.sdk .hover\:text-muted-foreground:hover {
  color: hsl(var(--muted-foreground)) !important;
}.sdk .hover\:text-primary:hover {
  color: rgb(var(--primary)) !important;
}.sdk .hover\:text-primary-foreground:hover {
  color: hsl(var(--primary-foreground)) !important;
}.sdk .hover\:text-white:hover {
  --tw-text-opacity: 1 !important;
  color: rgb(255 255 255 / var(--tw-text-opacity)) !important;
}.sdk .hover\:underline:hover {
  text-decoration-line: underline !important;
}.sdk .hover\:no-underline:hover {
  text-decoration-line: none !important;
}.sdk .hover\:opacity-100:hover {
  opacity: 1 !important;
}.sdk .focus\:border-ring:focus {
  border-color: hsl(var(--ring)) !important;
}.sdk .focus\:bg-accent:focus {
  background-color: hsl(var(--accent)) !important;
}.sdk .focus\:bg-primary:focus {
  background-color: rgb(var(--primary)) !important;
}.sdk .focus\:text-accent-foreground:focus {
  color: hsl(var(--accent-foreground)) !important;
}.sdk .focus\:text-primary-foreground:focus {
  color: hsl(var(--primary-foreground)) !important;
}.sdk .focus\:outline-none:focus {
  outline: 2px solid transparent !important;
  outline-offset: 2px !important;
}.sdk .focus\:outline-0:focus {
  outline-width: 0px !important;
}.sdk .focus-visible\:border-none:focus-visible {
  border-style: none !important;
}.sdk .focus-visible\:shadow-none:focus-visible {
  --tw-shadow: 0 0 #0000 !important;
  --tw-shadow-colored: 0 0 #0000 !important;
  box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow) !important;
}.sdk .focus-visible\:outline-none:focus-visible {
  outline: 2px solid transparent !important;
  outline-offset: 2px !important;
}.sdk .focus-visible\:ring-2:focus-visible {
  --tw-ring-offset-shadow: var(--tw-ring-inset) 0 0 0 var(--tw-ring-offset-width) var(--tw-ring-offset-color) !important;
  --tw-ring-shadow: var(--tw-ring-inset) 0 0 0 calc(2px + var(--tw-ring-offset-width)) var(--tw-ring-color) !important;
  box-shadow: var(--tw-ring-offset-shadow), var(--tw-ring-shadow), var(--tw-shadow, 0 0 #0000) !important;
}.sdk .focus-visible\:ring-ring:focus-visible {
  --tw-ring-color: hsl(var(--ring)) !important;
}.sdk .focus-visible\:ring-offset-2:focus-visible {
  --tw-ring-offset-width: 2px !important;
}.sdk .active\:bg-\[rgb\(5\2c 140\2c 224\)\]:active {
  --tw-bg-opacity: 1 !important;
  background-color: rgb(5 140 224 / var(--tw-bg-opacity)) !important;
}.sdk .active\:bg-destructive:active {
  background-color: hsl(var(--destructive)) !important;
}.sdk .active\:bg-primary:active {
  background-color: rgb(var(--primary)) !important;
}.sdk .active\:text-white:active {
  --tw-text-opacity: 1 !important;
  color: rgb(255 255 255 / var(--tw-text-opacity)) !important;
}.sdk .disabled\:pointer-events-none:disabled {
  pointer-events: none !important;
}.sdk .disabled\:cursor-not-allowed:disabled {
  cursor: not-allowed !important;
}.sdk .disabled\:opacity-50:disabled {
  opacity: 0.5 !important;
}.sdk .group:hover .group-hover\:opacity-100 {
  opacity: 1 !important;
}.sdk .group.destructive .group-\[\.destructive\]\:border-muted\/40 {
  border-color: hsl(var(--muted) / 0.4) !important;
}.sdk .group.toaster .group-\[\.toaster\]\:border-border {
  border-color: hsl(var(--border)) !important;
}.sdk .group.toast .group-\[\.toast\]\:bg-muted {
  background-color: hsl(var(--muted)) !important;
}.sdk .group.toast .group-\[\.toast\]\:bg-primary {
  background-color: rgb(var(--primary)) !important;
}.sdk .group.toaster .group-\[\.toaster\]\:bg-background {
  background-color: hsl(var(--background)) !important;
}.sdk .group.destructive .group-\[\.destructive\]\:text-red-300 {
  --tw-text-opacity: 1 !important;
  color: rgb(252 165 165 / var(--tw-text-opacity)) !important;
}.sdk .group.toast .group-\[\.toast\]\:text-muted-foreground {
  color: hsl(var(--muted-foreground)) !important;
}.sdk .group.toast .group-\[\.toast\]\:text-primary-foreground {
  color: hsl(var(--primary-foreground)) !important;
}.sdk .group.toaster .group-\[\.toaster\]\:text-foreground {
  color: hsl(var(--foreground)) !important;
}.sdk .group.toaster .group-\[\.toaster\]\:shadow-lg {
  --tw-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1) !important;
  --tw-shadow-colored: 0 10px 15px -3px var(--tw-shadow-color), 0 4px 6px -4px var(--tw-shadow-color) !important;
  box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow) !important;
}.sdk .group.destructive .group-\[\.destructive\]\:hover\:border-destructive\/30:hover {
  border-color: hsl(var(--destructive) / 0.3) !important;
}.sdk .group.destructive .group-\[\.destructive\]\:hover\:bg-destructive:hover {
  background-color: hsl(var(--destructive)) !important;
}.sdk .group.destructive .group-\[\.destructive\]\:hover\:text-destructive-foreground:hover {
  color: hsl(var(--destructive-foreground)) !important;
}.sdk .group.destructive .group-\[\.destructive\]\:hover\:text-red-50:hover {
  --tw-text-opacity: 1 !important;
  color: rgb(254 242 242 / var(--tw-text-opacity)) !important;
}.sdk .group.destructive .group-\[\.destructive\]\:focus\:ring-destructive:focus {
  --tw-ring-color: hsl(var(--destructive)) !important;
}.sdk .group.destructive .group-\[\.destructive\]\:focus\:ring-red-400:focus {
  --tw-ring-opacity: 1 !important;
  --tw-ring-color: rgb(248 113 113 / var(--tw-ring-opacity)) !important;
}.sdk .group.destructive .group-\[\.destructive\]\:focus\:ring-offset-red-600:focus {
  --tw-ring-offset-color: #dc2626 !important;
}.sdk .peer:disabled ~ .peer-disabled\:cursor-not-allowed {
  cursor: not-allowed !important;
}.sdk .peer:disabled ~ .peer-disabled\:opacity-70 {
  opacity: 0.7 !important;
}.sdk .aria-selected\:bg-accent[aria-selected="true"] {
  background-color: hsl(var(--accent)) !important;
}.sdk .aria-selected\:bg-accent\/50[aria-selected="true"] {
  background-color: hsl(var(--accent) / 0.5) !important;
}.sdk .aria-selected\:text-accent-foreground[aria-selected="true"] {
  color: hsl(var(--accent-foreground)) !important;
}.sdk .aria-selected\:text-muted-foreground[aria-selected="true"] {
  color: hsl(var(--muted-foreground)) !important;
}.sdk .aria-selected\:opacity-100[aria-selected="true"] {
  opacity: 1 !important;
}.sdk .aria-selected\:opacity-30[aria-selected="true"] {
  opacity: 0.3 !important;
}.sdk .data-\[disabled\]\:pointer-events-none[data-disabled] {
  pointer-events: none !important;
}.sdk .data-\[panel-group-direction\=vertical\]\:h-px[data-panel-group-direction=vertical] {
  height: 1px !important;
}.sdk .data-\[panel-group-direction\=vertical\]\:w-full[data-panel-group-direction=vertical] {
  width: 100% !important;
}.sdk .data-\[side\=bottom\]\:translate-y-1[data-side=bottom] {
  --tw-translate-y: 0.25rem !important;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y)) !important;
}.sdk .data-\[side\=left\]\:-translate-x-1[data-side=left] {
  --tw-translate-x: -0.25rem !important;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y)) !important;
}.sdk .data-\[side\=right\]\:translate-x-1[data-side=right] {
  --tw-translate-x: 0.25rem !important;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y)) !important;
}.sdk .data-\[side\=top\]\:-translate-y-1[data-side=top] {
  --tw-translate-y: -0.25rem !important;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y)) !important;
}.sdk .data-\[state\=checked\]\:translate-x-5[data-state=checked] {
  --tw-translate-x: 1.25rem !important;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y)) !important;
}.sdk .data-\[state\=unchecked\]\:translate-x-0[data-state=unchecked] {
  --tw-translate-x: 0px !important;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y)) !important;
}.sdk .data-\[swipe\=cancel\]\:translate-x-0[data-swipe=cancel] {
  --tw-translate-x: 0px !important;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y)) !important;
}.sdk .data-\[swipe\=end\]\:translate-x-\[var\(--radix-toast-swipe-end-x\)\][data-swipe=end] {
  --tw-translate-x: var(--radix-toast-swipe-end-x) !important;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y)) !important;
}.sdk .data-\[swipe\=move\]\:translate-x-\[var\(--radix-toast-swipe-move-x\)\][data-swipe=move] {
  --tw-translate-x: var(--radix-toast-swipe-move-x) !important;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y)) !important;
}@keyframes accordion-up {from {
    height: var(--radix-accordion-content-height);
  }to {
    height: 0;
  }
}.sdk .data-\[state\=closed\]\:animate-accordion-up[data-state=closed] {
  animation: accordion-up 0.2s ease-out !important;
}@keyframes accordion-down {from {
    height: 0;
  }to {
    height: var(--radix-accordion-content-height);
  }
}.sdk .data-\[state\=open\]\:animate-accordion-down[data-state=open] {
  animation: accordion-down 0.2s ease-out !important;
}.sdk .data-\[disabled\=true\]\:cursor-not-allowed[data-disabled=true] {
  cursor: not-allowed !important;
}.sdk .data-\[panel-group-direction\=vertical\]\:flex-col[data-panel-group-direction=vertical] {
  flex-direction: column !important;
}.sdk .data-\[state\=checked\]\:border-primary[data-state=checked] {
  border-color: rgb(var(--primary)) !important;
}.sdk .data-\[state\=active\]\:border-b-primary[data-state=active] {
  border-bottom-color: rgb(var(--primary)) !important;
}.sdk .data-\[active\]\:bg-accent\/50[data-active] {
  background-color: hsl(var(--accent) / 0.5) !important;
}.sdk .data-\[state\=active\]\:bg-background[data-state=active] {
  background-color: hsl(var(--background)) !important;
}.sdk .data-\[state\=checked\]\:bg-primary[data-state=checked] {
  background-color: rgb(var(--primary)) !important;
}.sdk .data-\[state\=on\]\:bg-accent[data-state=on] {
  background-color: hsl(var(--accent)) !important;
}.sdk .data-\[state\=open\]\:bg-accent[data-state=open] {
  background-color: hsl(var(--accent)) !important;
}.sdk .data-\[state\=open\]\:bg-accent\/50[data-state=open] {
  background-color: hsl(var(--accent) / 0.5) !important;
}.sdk .data-\[state\=open\]\:bg-secondary[data-state=open] {
  background-color: rgb(var(--secondary)) !important;
}.sdk .data-\[state\=selected\]\:bg-muted[data-state=selected] {
  background-color: hsl(var(--muted)) !important;
}.sdk .data-\[state\=unchecked\]\:bg-input[data-state=unchecked] {
  background-color: hsl(var(--input)) !important;
}.sdk .data-\[state\=active\]\:text-foreground[data-state=active] {
  color: hsl(var(--foreground)) !important;
}.sdk .data-\[state\=active\]\:text-primary[data-state=active] {
  color: rgb(var(--primary)) !important;
}.sdk .data-\[state\=checked\]\:text-primary-foreground[data-state=checked] {
  color: hsl(var(--primary-foreground)) !important;
}.sdk .data-\[state\=open\]\:text-accent-foreground[data-state=open] {
  color: hsl(var(--accent-foreground)) !important;
}.sdk .data-\[state\=open\]\:text-muted-foreground[data-state=open] {
  color: hsl(var(--muted-foreground)) !important;
}.sdk .data-\[disabled\=true\]\:opacity-50[data-disabled=true] {
  opacity: 0.5 !important;
}.sdk .data-\[disabled\]\:opacity-50[data-disabled] {
  opacity: 0.5 !important;
}.sdk .data-\[state\=active\]\:shadow-none[data-state=active] {
  --tw-shadow: 0 0 #0000 !important;
  --tw-shadow-colored: 0 0 #0000 !important;
  box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow) !important;
}.sdk .data-\[state\=active\]\:shadow-sm[data-state=active] {
  --tw-shadow: 0 1px 2px 0 rgb(0 0 0 / 0.05) !important;
  --tw-shadow-colored: 0 1px 2px 0 var(--tw-shadow-color) !important;
  box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow) !important;
}.sdk .data-\[swipe\=move\]\:transition-none[data-swipe=move] {
  transition-property: none !important;
}.sdk .data-\[state\=closed\]\:duration-300[data-state=closed] {
  transition-duration: 300ms !important;
}.sdk .data-\[state\=open\]\:duration-500[data-state=open] {
  transition-duration: 500ms !important;
}.sdk .data-\[motion\^\=from-\]\:animate-in[data-motion^=from-] {
  animation-name: enter !important;
  animation-duration: 150ms !important;
  --tw-enter-opacity: initial !important;
  --tw-enter-scale: initial !important;
  --tw-enter-rotate: initial !important;
  --tw-enter-translate-x: initial !important;
  --tw-enter-translate-y: initial !important;
}.sdk .data-\[state\=open\]\:animate-in[data-state=open] {
  animation-name: enter !important;
  animation-duration: 150ms !important;
  --tw-enter-opacity: initial !important;
  --tw-enter-scale: initial !important;
  --tw-enter-rotate: initial !important;
  --tw-enter-translate-x: initial !important;
  --tw-enter-translate-y: initial !important;
}.sdk .data-\[state\=visible\]\:animate-in[data-state=visible] {
  animation-name: enter !important;
  animation-duration: 150ms !important;
  --tw-enter-opacity: initial !important;
  --tw-enter-scale: initial !important;
  --tw-enter-rotate: initial !important;
  --tw-enter-translate-x: initial !important;
  --tw-enter-translate-y: initial !important;
}.sdk .data-\[motion\^\=to-\]\:animate-out[data-motion^=to-] {
  animation-name: exit !important;
  animation-duration: 150ms !important;
  --tw-exit-opacity: initial !important;
  --tw-exit-scale: initial !important;
  --tw-exit-rotate: initial !important;
  --tw-exit-translate-x: initial !important;
  --tw-exit-translate-y: initial !important;
}.sdk .data-\[state\=closed\]\:animate-out[data-state=closed] {
  animation-name: exit !important;
  animation-duration: 150ms !important;
  --tw-exit-opacity: initial !important;
  --tw-exit-scale: initial !important;
  --tw-exit-rotate: initial !important;
  --tw-exit-translate-x: initial !important;
  --tw-exit-translate-y: initial !important;
}.sdk .data-\[state\=hidden\]\:animate-out[data-state=hidden] {
  animation-name: exit !important;
  animation-duration: 150ms !important;
  --tw-exit-opacity: initial !important;
  --tw-exit-scale: initial !important;
  --tw-exit-rotate: initial !important;
  --tw-exit-translate-x: initial !important;
  --tw-exit-translate-y: initial !important;
}.sdk .data-\[swipe\=end\]\:animate-out[data-swipe=end] {
  animation-name: exit !important;
  animation-duration: 150ms !important;
  --tw-exit-opacity: initial !important;
  --tw-exit-scale: initial !important;
  --tw-exit-rotate: initial !important;
  --tw-exit-translate-x: initial !important;
  --tw-exit-translate-y: initial !important;
}.sdk .data-\[motion\^\=from-\]\:fade-in[data-motion^=from-] {
  --tw-enter-opacity: 0 !important;
}.sdk .data-\[motion\^\=to-\]\:fade-out[data-motion^=to-] {
  --tw-exit-opacity: 0 !important;
}.sdk .data-\[state\=closed\]\:fade-out-0[data-state=closed] {
  --tw-exit-opacity: 0 !important;
}.sdk .data-\[state\=closed\]\:fade-out-80[data-state=closed] {
  --tw-exit-opacity: 0.8 !important;
}.sdk .data-\[state\=hidden\]\:fade-out[data-state=hidden] {
  --tw-exit-opacity: 0 !important;
}.sdk .data-\[state\=open\]\:fade-in-0[data-state=open] {
  --tw-enter-opacity: 0 !important;
}.sdk .data-\[state\=visible\]\:fade-in[data-state=visible] {
  --tw-enter-opacity: 0 !important;
}.sdk .data-\[state\=closed\]\:zoom-out-95[data-state=closed] {
  --tw-exit-scale: .95 !important;
}.sdk .data-\[state\=open\]\:zoom-in-90[data-state=open] {
  --tw-enter-scale: .9 !important;
}.sdk .data-\[state\=open\]\:zoom-in-95[data-state=open] {
  --tw-enter-scale: .95 !important;
}.sdk .data-\[motion\=from-end\]\:slide-in-from-right-52[data-motion=from-end] {
  --tw-enter-translate-x: 13rem !important;
}.sdk .data-\[motion\=from-start\]\:slide-in-from-left-52[data-motion=from-start] {
  --tw-enter-translate-x: -13rem !important;
}.sdk .data-\[motion\=to-end\]\:slide-out-to-right-52[data-motion=to-end] {
  --tw-exit-translate-x: 13rem !important;
}.sdk .data-\[motion\=to-start\]\:slide-out-to-left-52[data-motion=to-start] {
  --tw-exit-translate-x: -13rem !important;
}.sdk .data-\[side\=bottom\]\:slide-in-from-top-2[data-side=bottom] {
  --tw-enter-translate-y: -0.5rem !important;
}.sdk .data-\[side\=left\]\:slide-in-from-right-2[data-side=left] {
  --tw-enter-translate-x: 0.5rem !important;
}.sdk .data-\[side\=right\]\:slide-in-from-left-2[data-side=right] {
  --tw-enter-translate-x: -0.5rem !important;
}.sdk .data-\[side\=top\]\:slide-in-from-bottom-2[data-side=top] {
  --tw-enter-translate-y: 0.5rem !important;
}.sdk .data-\[state\=closed\]\:slide-out-to-bottom[data-state=closed] {
  --tw-exit-translate-y: 100% !important;
}.sdk .data-\[state\=closed\]\:slide-out-to-left[data-state=closed] {
  --tw-exit-translate-x: -100% !important;
}.sdk .data-\[state\=closed\]\:slide-out-to-left-1\/2[data-state=closed] {
  --tw-exit-translate-x: -50% !important;
}.sdk .data-\[state\=closed\]\:slide-out-to-right[data-state=closed] {
  --tw-exit-translate-x: 100% !important;
}.sdk .data-\[state\=closed\]\:slide-out-to-right-full[data-state=closed] {
  --tw-exit-translate-x: 100% !important;
}.sdk .data-\[state\=closed\]\:slide-out-to-top[data-state=closed] {
  --tw-exit-translate-y: -100% !important;
}.sdk .data-\[state\=closed\]\:slide-out-to-top-\[48\%\][data-state=closed] {
  --tw-exit-translate-y: -48% !important;
}.sdk .data-\[state\=open\]\:slide-in-from-bottom[data-state=open] {
  --tw-enter-translate-y: 100% !important;
}.sdk .data-\[state\=open\]\:slide-in-from-left[data-state=open] {
  --tw-enter-translate-x: -100% !important;
}.sdk .data-\[state\=open\]\:slide-in-from-left-1\/2[data-state=open] {
  --tw-enter-translate-x: -50% !important;
}.sdk .data-\[state\=open\]\:slide-in-from-right[data-state=open] {
  --tw-enter-translate-x: 100% !important;
}.sdk .data-\[state\=open\]\:slide-in-from-top[data-state=open] {
  --tw-enter-translate-y: -100% !important;
}.sdk .data-\[state\=open\]\:slide-in-from-top-\[48\%\][data-state=open] {
  --tw-enter-translate-y: -48% !important;
}.sdk .data-\[state\=open\]\:slide-in-from-top-full[data-state=open] {
  --tw-enter-translate-y: -100% !important;
}.sdk .data-\[state\=closed\]\:duration-300[data-state=closed] {
  animation-duration: 300ms !important;
}.sdk .data-\[state\=open\]\:duration-500[data-state=open] {
  animation-duration: 500ms !important;
}.sdk .data-\[panel-group-direction\=vertical\]\:after\:left-0[data-panel-group-direction=vertical]::after {
  content: var(--tw-content) !important;
  left: 0px !important;
}.sdk .data-\[panel-group-direction\=vertical\]\:after\:h-1[data-panel-group-direction=vertical]::after {
  content: var(--tw-content) !important;
  height: 0.25rem !important;
}.sdk .data-\[panel-group-direction\=vertical\]\:after\:w-full[data-panel-group-direction=vertical]::after {
  content: var(--tw-content) !important;
  width: 100% !important;
}.sdk .data-\[panel-group-direction\=vertical\]\:after\:-translate-y-1\/2[data-panel-group-direction=vertical]::after {
  content: var(--tw-content) !important;
  --tw-translate-y: -50% !important;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y)) !important;
}.sdk .data-\[panel-group-direction\=vertical\]\:after\:translate-x-0[data-panel-group-direction=vertical]::after {
  content: var(--tw-content) !important;
  --tw-translate-x: 0px !important;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y)) !important;
}.sdk .group[data-state=open] .group-data-\[state\=open\]\:rotate-180 {
  --tw-rotate: 180deg !important;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y)) !important;
}.dark\:border-r:is(.dark *) {
  border-right-width: 1px !important;
}.dark\:border-none:is(.dark *) {
  border-style: none !important;
}.dark\:border-destructive:is(.dark *) {
  border-color: hsl(var(--destructive)) !important;
}.dark\:text-foreground:is(.dark *) {
  color: hsl(var(--foreground)) !important;
}.dark\:shadow-none:is(.dark *) {
  --tw-shadow: 0 0 #0000 !important;
  --tw-shadow-colored: 0 0 #0000 !important;
  box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow) !important;
}@media (min-width: 320px) {.sdk .xxs\:px-6 {
    padding-left: 1.5rem !important;
    padding-right: 1.5rem !important;
  }.sdk .xxs\:py-4 {
    padding-top: 1rem !important;
    padding-bottom: 1rem !important;
  }
}@media (min-width: 480px) {.sdk .xs\:block {
    display: block !important;
  }.sdk .xs\:flex {
    display: flex !important;
  }.sdk .xs\:h-72 {
    height: 18rem !important;
  }.sdk .xs\:max-h-72 {
    max-height: 18rem !important;
  }.sdk .xs\:w-\[240px\] {
    width: 240px !important;
  }.sdk .xs\:w-\[400px\] {
    width: 400px !important;
  }.sdk .xs\:w-\[90\%\] {
    width: 90% !important;
  }.sdk .xs\:w-full {
    width: 100% !important;
  }.sdk .xs\:grid-cols-2 {
    grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
  }.sdk .xs\:justify-between {
    justify-content: space-between !important;
  }.sdk .xs\:gap-1 {
    gap: 0.25rem !important;
  }.sdk .xs\:px-8 {
    padding-left: 2rem !important;
    padding-right: 2rem !important;
  }.sdk .xs\:py-4 {
    padding-top: 1rem !important;
    padding-bottom: 1rem !important;
  }.sdk .xs\:text-base {
    font-size: 1rem !important;
    line-height: 1.5rem !important;
  }.sdk .xs\:text-xs {
    font-size: 0.75rem !important;
    line-height: 1rem !important;
  }
}@media (min-width: 640px) {.sdk .sm\:sticky {
    position: sticky !important;
  }.sdk .sm\:bottom-0 {
    bottom: 0px !important;
  }.sdk .sm\:right-0 {
    right: 0px !important;
  }.sdk .sm\:right-10 {
    right: 2.5rem !important;
  }.sdk .sm\:top-10 {
    top: 2.5rem !important;
  }.sdk .sm\:top-auto {
    top: auto !important;
  }.sdk .sm\:-mx-8 {
    margin-left: -2rem !important;
    margin-right: -2rem !important;
  }.sdk .sm\:my-3 {
    margin-top: 0.75rem !important;
    margin-bottom: 0.75rem !important;
  }.sdk .sm\:mb-20 {
    margin-bottom: 5rem !important;
  }.sdk .sm\:ml-6 {
    margin-left: 1.5rem !important;
  }.sdk .sm\:ml-auto {
    margin-left: auto !important;
  }.sdk .sm\:mr-0 {
    margin-right: 0px !important;
  }.sdk .sm\:mr-4 {
    margin-right: 1rem !important;
  }.sdk .sm\:mr-auto {
    margin-right: auto !important;
  }.sdk .sm\:mt-0 {
    margin-top: 0px !important;
  }.sdk .sm\:mt-4 {
    margin-top: 1rem !important;
  }.sdk .sm\:mt-8 {
    margin-top: 2rem !important;
  }.sdk .sm\:block {
    display: block !important;
  }.sdk .sm\:flex {
    display: flex !important;
  }.sdk .sm\:hidden {
    display: none !important;
  }.sdk .sm\:h-10 {
    height: 2.5rem !important;
  }.sdk .sm\:h-32 {
    height: 8rem !important;
  }.sdk .sm\:h-36 {
    height: 9rem !important;
  }.sdk .sm\:h-40 {
    height: 10rem !important;
  }.sdk .sm\:h-52 {
    height: 13rem !important;
  }.sdk .sm\:h-56 {
    height: 14rem !important;
  }.sdk .sm\:h-60 {
    height: 15rem !important;
  }.sdk .sm\:h-\[640px\] {
    height: 640px !important;
  }.sdk .sm\:h-\[calc\(100vh-56px-72px\)\] {
    height: calc(100vh - 56px - 72px) !important;
  }.sdk .sm\:max-h-40 {
    max-height: 10rem !important;
  }.sdk .sm\:max-h-60 {
    max-height: 15rem !important;
  }.sdk .sm\:max-h-\[30vh\] {
    max-height: 30vh !important;
  }.sdk .sm\:\!w-52 {
    width: 13rem !important;
  }.sdk .sm\:w-1\/3 {
    width: 33.333333% !important;
  }.sdk .sm\:w-2\/3 {
    width: 66.666667% !important;
  }.sdk .sm\:w-3\/4 {
    width: 75% !important;
  }.sdk .sm\:w-3\/5 {
    width: 60% !important;
  }.sdk .sm\:w-40 {
    width: 10rem !important;
  }.sdk .sm\:w-96 {
    width: 24rem !important;
  }.sdk .sm\:w-\[80\%\] {
    width: 80% !important;
  }.sdk .sm\:w-\[initial\] {
    width: initial !important;
  }.sdk .sm\:w-auto {
    width: auto !important;
  }.sdk .sm\:min-w-\[160px\] {
    min-width: 160px !important;
  }.sdk .sm\:min-w-\[320px\] {
    min-width: 320px !important;
  }.sdk .sm\:min-w-\[355px\] {
    min-width: 355px !important;
  }.sdk .sm\:min-w-\[420px\] {
    min-width: 420px !important;
  }.sdk .sm\:min-w-\[480px\] {
    min-width: 480px !important;
  }.sdk .sm\:max-w-40 {
    max-width: 10rem !important;
  }.sdk .sm\:max-w-\[40\%\] {
    max-width: 40% !important;
  }.sdk .sm\:max-w-md {
    max-width: 28rem !important;
  }.sdk .sm\:max-w-sm {
    max-width: 24rem !important;
  }.sdk .sm\:flex-none {
    flex: none !important;
  }.sdk .sm\:flex-row {
    flex-direction: row !important;
  }.sdk .sm\:flex-col {
    flex-direction: column !important;
  }.sdk .sm\:items-start {
    align-items: flex-start !important;
  }.sdk .sm\:items-center {
    align-items: center !important;
  }.sdk .sm\:justify-end {
    justify-content: flex-end !important;
  }.sdk .sm\:justify-center {
    justify-content: center !important;
  }.sdk .sm\:gap-0 {
    gap: 0px !important;
  }.sdk .sm\:gap-1 {
    gap: 0.25rem !important;
  }.sdk .sm\:gap-2 {
    gap: 0.5rem !important;
  }.sdk .sm\:gap-2\.5 {
    gap: 0.625rem !important;
  }.sdk .sm\:gap-4 {
    gap: 1rem !important;
  }.sdk .sm\:gap-5 {
    gap: 1.25rem !important;
  }.sdk .sm\:gap-6 {
    gap: 1.5rem !important;
  }.sdk .sm\:space-x-2 > :not([hidden]) ~ :not([hidden]) {
    --tw-space-x-reverse: 0 !important;
    margin-right: calc(0.5rem * var(--tw-space-x-reverse)) !important;
    margin-left: calc(0.5rem * calc(1 - var(--tw-space-x-reverse))) !important;
  }.sdk .sm\:space-x-4 > :not([hidden]) ~ :not([hidden]) {
    --tw-space-x-reverse: 0 !important;
    margin-right: calc(1rem * var(--tw-space-x-reverse)) !important;
    margin-left: calc(1rem * calc(1 - var(--tw-space-x-reverse))) !important;
  }.sdk .sm\:space-y-0 > :not([hidden]) ~ :not([hidden]) {
    --tw-space-y-reverse: 0 !important;
    margin-top: calc(0px * calc(1 - var(--tw-space-y-reverse))) !important;
    margin-bottom: calc(0px * var(--tw-space-y-reverse)) !important;
  }.sdk .sm\:rounded-lg {
    border-radius: var(--radius) !important;
  }.sdk .sm\:border-l {
    border-left-width: 1px !important;
  }.sdk .sm\:bg-background {
    background-color: hsl(var(--background)) !important;
  }.sdk .sm\:p-2 {
    padding: 0.5rem !important;
  }.sdk .sm\:p-4 {
    padding: 1rem !important;
  }.sdk .sm\:p-8 {
    padding: 2rem !important;
  }.sdk .sm\:px-0 {
    padding-left: 0px !important;
    padding-right: 0px !important;
  }.sdk .sm\:px-10 {
    padding-left: 2.5rem !important;
    padding-right: 2.5rem !important;
  }.sdk .sm\:px-12 {
    padding-left: 3rem !important;
    padding-right: 3rem !important;
  }.sdk .sm\:px-16 {
    padding-left: 4rem !important;
    padding-right: 4rem !important;
  }.sdk .sm\:px-2 {
    padding-left: 0.5rem !important;
    padding-right: 0.5rem !important;
  }.sdk .sm\:px-20 {
    padding-left: 5rem !important;
    padding-right: 5rem !important;
  }.sdk .sm\:px-4 {
    padding-left: 1rem !important;
    padding-right: 1rem !important;
  }.sdk .sm\:px-6 {
    padding-left: 1.5rem !important;
    padding-right: 1.5rem !important;
  }.sdk .sm\:px-8 {
    padding-left: 2rem !important;
    padding-right: 2rem !important;
  }.sdk .sm\:py-1 {
    padding-top: 0.25rem !important;
    padding-bottom: 0.25rem !important;
  }.sdk .sm\:py-12 {
    padding-top: 3rem !important;
    padding-bottom: 3rem !important;
  }.sdk .sm\:py-6 {
    padding-top: 1.5rem !important;
    padding-bottom: 1.5rem !important;
  }.sdk .sm\:py-8 {
    padding-top: 2rem !important;
    padding-bottom: 2rem !important;
  }.sdk .sm\:pb-24 {
    padding-bottom: 6rem !important;
  }.sdk .sm\:pb-6 {
    padding-bottom: 1.5rem !important;
  }.sdk .sm\:pl-20 {
    padding-left: 5rem !important;
  }.sdk .sm\:pl-8 {
    padding-left: 2rem !important;
  }.sdk .sm\:pr-20 {
    padding-right: 5rem !important;
  }.sdk .sm\:pr-4 {
    padding-right: 1rem !important;
  }.sdk .sm\:pt-0 {
    padding-top: 0px !important;
  }.sdk .sm\:pt-10 {
    padding-top: 2.5rem !important;
  }.sdk .sm\:pt-16 {
    padding-top: 4rem !important;
  }.sdk .sm\:pt-8 {
    padding-top: 2rem !important;
  }.sdk .sm\:text-left {
    text-align: left !important;
  }.sdk .sm\:text-2xl {
    font-size: 1.5rem !important;
    line-height: 2rem !important;
  }.sdk .sm\:text-3xl {
    font-size: 1.875rem !important;
    line-height: 2.25rem !important;
  }.sdk .sm\:text-4xl {
    font-size: 2.25rem !important;
    line-height: 2.5rem !important;
  }.sdk .sm\:text-5xl {
    font-size: 3rem !important;
    line-height: 1 !important;
  }.sdk .sm\:text-base {
    font-size: 1rem !important;
    line-height: 1.5rem !important;
  }.sdk .sm\:text-lg {
    font-size: 1.125rem !important;
    line-height: 1.75rem !important;
  }.sdk .sm\:text-sm {
    font-size: 0.875rem !important;
    line-height: 1.25rem !important;
  }.sdk .sm\:text-xl {
    font-size: 1.25rem !important;
    line-height: 1.75rem !important;
  }.sdk .sm\:font-semibold {
    font-weight: 600 !important;
  }.sdk .sm\:text-foreground {
    color: hsl(var(--foreground)) !important;
  }.sdk .sm\:\[text-shadow\:0px_4px_4px_rgba\(0\2c 0\2c 0\2c 0\.25\)\] {
    text-shadow: 0px 4px 4px rgba(0,0,0,0.25) !important;
  }.sdk .sm\:hover\:bg-background-tertiary:hover {
    background-color: hsl(var(--background-tertiary)) !important;
  }.sdk .sm\:hover\:opacity-80:hover {
    opacity: 0.8 !important;
  }.sdk .data-\[state\=open\]\:sm\:slide-in-from-bottom-full[data-state=open] {
    --tw-enter-translate-y: 100% !important;
  }
}@media (min-width: 768px) {.sdk .md\:col-span-4 {
    grid-column: span 4 / span 4 !important;
  }.sdk .md\:ml-16 {
    margin-left: 4rem !important;
  }.sdk .md\:mt-8 {
    margin-top: 2rem !important;
  }.sdk .md\:inline {
    display: inline !important;
  }.sdk .md\:h-40 {
    height: 10rem !important;
  }.sdk .md\:h-\[calc\(100vh-56px-72px\)\] {
    height: calc(100vh - 56px - 72px) !important;
  }.sdk .md\:\!w-40 {
    width: 10rem !important;
  }.sdk .md\:w-1\/2 {
    width: 50% !important;
  }.sdk .md\:w-\[240px\] {
    width: 240px !important;
  }.sdk .md\:w-\[360px\] {
    width: 360px !important;
  }.sdk .md\:w-\[400px\] {
    width: 400px !important;
  }.sdk .md\:w-\[668px\] {
    width: 668px !important;
  }.sdk .md\:w-\[70\%\] {
    width: 70% !important;
  }.sdk .md\:w-\[var\(--radix-navigation-menu-viewport-width\)\] {
    width: var(--radix-navigation-menu-viewport-width) !important;
  }.sdk .md\:max-w-\[30\%\] {
    max-width: 30% !important;
  }.sdk .md\:max-w-\[420px\] {
    max-width: 420px !important;
  }.sdk .md\:max-w-\[618px\] {
    max-width: 618px !important;
  }.sdk .md\:flex-\[2\] {
    flex: 2 !important;
  }.sdk .md\:grid-cols-1 {
    grid-template-columns: repeat(1, minmax(0, 1fr)) !important;
  }.sdk .md\:grid-cols-2 {
    grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
  }.sdk .md\:grid-cols-3 {
    grid-template-columns: repeat(3, minmax(0, 1fr)) !important;
  }.sdk .md\:flex-row {
    flex-direction: row !important;
  }.sdk .md\:flex-col {
    flex-direction: column !important;
  }.sdk .md\:gap-0 {
    gap: 0px !important;
  }.sdk .md\:gap-2 {
    gap: 0.5rem !important;
  }.sdk .md\:gap-6 {
    gap: 1.5rem !important;
  }.sdk .md\:gap-8 {
    gap: 2rem !important;
  }.sdk .md\:self-center {
    align-self: center !important;
  }.sdk .md\:p-2 {
    padding: 0.5rem !important;
  }.sdk .md\:px-20 {
    padding-left: 5rem !important;
    padding-right: 5rem !important;
  }.sdk .md\:px-28 {
    padding-left: 7rem !important;
    padding-right: 7rem !important;
  }.sdk .md\:py-12 {
    padding-top: 3rem !important;
    padding-bottom: 3rem !important;
  }.sdk .md\:py-20 {
    padding-top: 5rem !important;
    padding-bottom: 5rem !important;
  }.sdk .md\:pt-8 {
    padding-top: 2rem !important;
  }.sdk .md\:text-5xl {
    font-size: 3rem !important;
    line-height: 1 !important;
  }
}@media (min-width: 1024px) {.sdk .lg\:-mt-40 {
    margin-top: -10rem !important;
  }.sdk .lg\:mb-0 {
    margin-bottom: 0px !important;
  }.sdk .lg\:flex {
    display: flex !important;
  }.sdk .lg\:hidden {
    display: none !important;
  }.sdk .lg\:h-32 {
    height: 8rem !important;
  }.sdk .lg\:w-1\/3 {
    width: 33.333333% !important;
  }.sdk .lg\:max-w-\[40vw\] {
    max-width: 40vw !important;
  }.sdk .lg\:max-w-none {
    max-width: none !important;
  }.sdk .lg\:grid-cols-2 {
    grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
  }.sdk .lg\:grid-cols-3 {
    grid-template-columns: repeat(3, minmax(0, 1fr)) !important;
  }.sdk .lg\:grid-cols-5 {
    grid-template-columns: repeat(5, minmax(0, 1fr)) !important;
  }.sdk .lg\:flex-row {
    flex-direction: row !important;
  }.sdk .lg\:flex-col {
    flex-direction: column !important;
  }.sdk .lg\:gap-4 {
    gap: 1rem !important;
  }.sdk .lg\:gap-6 {
    gap: 1.5rem !important;
  }.sdk .lg\:p-8 {
    padding: 2rem !important;
  }.sdk .lg\:px-0 {
    padding-left: 0px !important;
    padding-right: 0px !important;
  }.sdk .lg\:py-1 {
    padding-top: 0.25rem !important;
    padding-bottom: 0.25rem !important;
  }.sdk .lg\:text-4xl {
    font-size: 2.25rem !important;
    line-height: 2.5rem !important;
  }.sdk .lg\:text-5xl {
    font-size: 3rem !important;
    line-height: 1 !important;
  }.sdk .lg\:text-6xl {
    font-size: 3.75rem !important;
    line-height: 1 !important;
  }
}@media (min-width: 1280px) {.sdk .xl\:-top-7 {
    top: -1.75rem !important;
  }.sdk .xl\:h-14 {
    height: 3.5rem !important;
  }.sdk .xl\:w-1\/4 {
    width: 25% !important;
  }.sdk .xl\:w-14 {
    width: 3.5rem !important;
  }.sdk .xl\:max-w-lg {
    max-width: 32rem !important;
  }.sdk .xl\:grid-cols-2 {
    grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
  }.sdk .xl\:grid-cols-3 {
    grid-template-columns: repeat(3, minmax(0, 1fr)) !important;
  }.sdk .xl\:pr-20 {
    padding-right: 5rem !important;
  }.sdk .xl\:text-xl {
    font-size: 1.25rem !important;
    line-height: 1.75rem !important;
  }
}@media (min-width: 1400px) {.sdk .\32xl\:-top-10 {
    top: -2.5rem !important;
  }.sdk .\32xl\:block {
    display: block !important;
  }.sdk .\32xl\:h-20 {
    height: 5rem !important;
  }.sdk .\32xl\:w-20 {
    width: 5rem !important;
  }.sdk .\32xl\:grid-cols-3 {
    grid-template-columns: repeat(3, minmax(0, 1fr)) !important;
  }.sdk .\32xl\:text-2xl {
    font-size: 1.5rem !important;
    line-height: 2rem !important;
  }
}@media (min-width: 1760px) {.sdk .\33xl\:grid-cols-6 {
    grid-template-columns: repeat(6, minmax(0, 1fr)) !important;
  }
}.sdk .first\:\[\&\:has\(\[aria-selected\]\)\]\:rounded-l-md:has([aria-selected]):first-child {
  border-top-left-radius: calc(var(--radius) - 2px) !important;
  border-bottom-left-radius: calc(var(--radius) - 2px) !important;
}.sdk .last\:\[\&\:has\(\[aria-selected\]\)\]\:rounded-r-md:has([aria-selected]):last-child {
  border-top-right-radius: calc(var(--radius) - 2px) !important;
  border-bottom-right-radius: calc(var(--radius) - 2px) !important;
}.sdk .\[\&\:has\(\[aria-selected\]\.day-outside\)\]\:bg-accent\/50:has([aria-selected].day-outside) {
  background-color: hsl(var(--accent) / 0.5) !important;
}.sdk .\[\&\:has\(\[aria-selected\]\.day-range-end\)\]\:rounded-r-md:has([aria-selected].day-range-end) {
  border-top-right-radius: calc(var(--radius) - 2px) !important;
  border-bottom-right-radius: calc(var(--radius) - 2px) !important;
}.sdk .\[\&\:has\(\[role\=checkbox\]\)\]\:pr-0:has([role=checkbox]) {
  padding-right: 0px !important;
}.sdk .\[\&\>span\]\:line-clamp-1>span {
  overflow: hidden !important;
  display: -webkit-box !important;
  -webkit-box-orient: vertical !important;
  -webkit-line-clamp: 1 !important;
}.sdk .\[\&\>svg\+div\]\:translate-y-\[-3px\]>svg+div {
  --tw-translate-y: -3px !important;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y)) !important;
}.sdk .\[\&\>svg\]\:absolute>svg {
  position: absolute !important;
}.sdk .\[\&\>svg\]\:left-4>svg {
  left: 1rem !important;
}.sdk .\[\&\>svg\]\:top-4>svg {
  top: 1rem !important;
}.sdk .\[\&\>svg\]\:size-3\.5>svg {
  width: 0.875rem !important;
  height: 0.875rem !important;
}.sdk .\[\&\>svg\]\:text-destructive>svg {
  color: hsl(var(--destructive)) !important;
}.sdk .\[\&\>svg\]\:text-foreground>svg {
  color: hsl(var(--foreground)) !important;
}.sdk .\[\&\>svg\~\*\]\:pl-7>svg~* {
  padding-left: 1.75rem !important;
}.sdk .\[\&\>tr\]\:last\:border-b-0:last-child>tr {
  border-bottom-width: 0px !important;
}.sdk .\[\&\[data-panel-group-direction\=vertical\]\>div\]\:rotate-90[data-panel-group-direction=vertical]>div {
  --tw-rotate: 90deg !important;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y)) !important;
}.sdk .\[\&\[data-state\=open\]\>svg\]\:rotate-180[data-state=open]>svg {
  --tw-rotate: 180deg !important;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y)) !important;
}.sdk .\[\&_\[cmdk-group-heading\]\]\:px-2 [cmdk-group-heading] {
  padding-left: 0.5rem !important;
  padding-right: 0.5rem !important;
}.sdk .\[\&_\[cmdk-group-heading\]\]\:py-1\.5 [cmdk-group-heading] {
  padding-top: 0.375rem !important;
  padding-bottom: 0.375rem !important;
}.sdk .\[\&_\[cmdk-group-heading\]\]\:text-xs [cmdk-group-heading] {
  font-size: 0.75rem !important;
  line-height: 1rem !important;
}.sdk .\[\&_\[cmdk-group-heading\]\]\:font-medium [cmdk-group-heading] {
  font-weight: 500 !important;
}.sdk .\[\&_\[cmdk-group-heading\]\]\:text-muted-foreground [cmdk-group-heading] {
  color: hsl(var(--muted-foreground)) !important;
}.sdk .\[\&_\[cmdk-group\]\:not\(\[hidden\]\)_\~\[cmdk-group\]\]\:pt-0 [cmdk-group]:not([hidden]) ~[cmdk-group] {
  padding-top: 0px !important;
}.sdk .\[\&_\[cmdk-group\]\]\:px-2 [cmdk-group] {
  padding-left: 0.5rem !important;
  padding-right: 0.5rem !important;
}.sdk .\[\&_\[cmdk-input-wrapper\]_svg\]\:h-5 [cmdk-input-wrapper] svg {
  height: 1.25rem !important;
}.sdk .\[\&_\[cmdk-input-wrapper\]_svg\]\:w-5 [cmdk-input-wrapper] svg {
  width: 1.25rem !important;
}.sdk .\[\&_\[cmdk-input\]\]\:h-12 [cmdk-input] {
  height: 3rem !important;
}.sdk .\[\&_\[cmdk-item\]\]\:px-2 [cmdk-item] {
  padding-left: 0.5rem !important;
  padding-right: 0.5rem !important;
}.sdk .\[\&_\[cmdk-item\]\]\:py-3 [cmdk-item] {
  padding-top: 0.75rem !important;
  padding-bottom: 0.75rem !important;
}.sdk .\[\&_\[cmdk-item\]_svg\]\:h-5 [cmdk-item] svg {
  height: 1.25rem !important;
}.sdk .\[\&_\[cmdk-item\]_svg\]\:w-5 [cmdk-item] svg {
  width: 1.25rem !important;
}.sdk .\[\&_p\]\:leading-relaxed p {
  line-height: 1.625 !important;
}.sdk .\[\&_path\]\:stroke-card-foreground path {
  stroke: hsl(var(--card-foreground)) !important;
}.sdk .\[\&_path\]\:stroke-current path {
  stroke: currentColor !important;
}.sdk .\[\&_tr\:last-child\]\:border-0 tr:last-child {
  border-width: 0px !important;
}.sdk .\[\&_tr\]\:border-b tr {
  border-bottom-width: 1px !important;
}
</style>

      <!-- React -->
      <script src="./robust_division_calculator_files/application-c554b60118504579ac85.js.download"></script>
      <link rel="stylesheet" media="screen" href="./robust_division_calculator_files/application-3873991c.css">


  <style>.sdk .rdp {
  --rdp-cell-size: 40px; /* Size of the day cells. */
  --rdp-caption-font-size: 18px; /* Font size for the caption labels. */
  --rdp-accent-color: #0000ff; /* Accent color for the background of selected days. */
  --rdp-background-color: #e7edff; /* Background color for the hovered/focused elements. */
  --rdp-accent-color-dark: #3003e1; /* Accent color for the background of selected days (to use in dark-mode). */
  --rdp-background-color-dark: #180270; /* Background color for the hovered/focused elements (to use in dark-mode). */
  --rdp-outline: 2px solid var(--rdp-accent-color); /* Outline border for focused elements */
  --rdp-outline-selected: 3px solid var(--rdp-accent-color); /* Outline border for focused _and_ selected elements */
  --rdp-selected-color: #fff; /* Color of selected day text */

  margin: 1em;
}

/* Hide elements for devices that are not screen readers */

.sdk .rdp-vhidden {
  box-sizing: border-box;
  margin: 0;
  background: transparent;
  -moz-appearance: none;
  -webkit-appearance: none;
  appearance: none;
  position: absolute !important;
  top: 0;
  width: 1px !important;
  height: 1px !important;
  padding: 0 !important;
  overflow: hidden !important;
  clip: rect(1px, 1px, 1px, 1px) !important;
  border: 0 !important;
}

/* Buttons */

.sdk .rdp-button_reset {
  appearance: none;
  position: relative;
  margin: 0;
  padding: 0;
  cursor: default;
  color: inherit;
  background: none;
  font: inherit;

  -moz-appearance: none;
  -webkit-appearance: none;
}

.sdk .rdp-button_reset:focus-visible {
  /* Make sure to reset outline only when :focus-visible is supported */
  outline: none;
}

.sdk .rdp-button {
  border: 2px solid transparent;
}

.sdk .rdp-button[disabled]:not(.rdp-day_selected) {
  opacity: 0.25;
}

.sdk .rdp-button:not([disabled]) {
  cursor: pointer;
}

.sdk .rdp-button:focus-visible:not([disabled]) {
  color: inherit;
  background-color: var(--rdp-background-color);
  border: var(--rdp-outline);
}

.sdk .rdp-button:hover:not([disabled]):not(.rdp-day_selected) {
  background-color: var(--rdp-background-color);
}

.sdk .rdp-months {
  display: flex;
}

.sdk .rdp-month {
  margin: 0 1em;
}

.sdk .rdp-month:first-child {
  margin-left: 0;
}

.sdk .rdp-month:last-child {
  margin-right: 0;
}

.sdk .rdp-table {
  margin: 0;
  max-width: calc(var(--rdp-cell-size) * 7);
  border-collapse: collapse;
}

.sdk .rdp-with_weeknumber .rdp-table {
  max-width: calc(var(--rdp-cell-size) * 8);
  border-collapse: collapse;
}

.sdk .rdp-caption {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0;
  text-align: left;
}

.sdk .rdp-multiple_months .rdp-caption {
  position: relative;
  display: block;
  text-align: center;
}

.sdk .rdp-caption_dropdowns {
  position: relative;
  display: inline-flex;
}

.sdk .rdp-caption_label {
  position: relative;
  z-index: 1;
  display: inline-flex;
  align-items: center;
  margin: 0;
  padding: 0 0.25em;
  white-space: nowrap;
  color: currentColor;
  border: 0;
  border: 2px solid transparent;
  font-family: inherit;
  font-size: var(--rdp-caption-font-size);
  font-weight: bold;
}

.sdk .rdp-nav {
  white-space: nowrap;
}

.sdk .rdp-multiple_months .rdp-caption_start .rdp-nav {
  position: absolute;
  top: 50%;
  left: 0;
  transform: translateY(-50%);
}

.sdk .rdp-multiple_months .rdp-caption_end .rdp-nav {
  position: absolute;
  top: 50%;
  right: 0;
  transform: translateY(-50%);
}

.sdk .rdp-nav_button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: var(--rdp-cell-size);
  height: var(--rdp-cell-size);
  padding: 0.25em;
  border-radius: 100%;
}

/* ---------- */

/* Dropdowns  */

/* ---------- */

.sdk .rdp-dropdown_year,
.sdk .rdp-dropdown_month {
  position: relative;
  display: inline-flex;
  align-items: center;
}

.sdk .rdp-dropdown {
  -webkit-appearance: none;
     -moz-appearance: none;
          appearance: none;
  position: absolute;
  z-index: 2;
  top: 0;
  bottom: 0;
  left: 0;
  width: 100%;
  margin: 0;
  padding: 0;
  cursor: inherit;
  opacity: 0;
  border: none;
  background-color: transparent;
  font-family: inherit;
  font-size: inherit;
  line-height: inherit;
}

.sdk .rdp-dropdown[disabled] {
  opacity: unset;
  color: unset;
}

.sdk .rdp-dropdown:focus-visible:not([disabled]) + .rdp-caption_label {
  background-color: var(--rdp-background-color);
  border: var(--rdp-outline);
  border-radius: 6px;
}

.sdk .rdp-dropdown_icon {
  margin: 0 0 0 5px;
}

.sdk .rdp-head {
  border: 0;
}

.sdk .rdp-head_row,
.sdk .rdp-row {
  height: 100%;
}

.sdk .rdp-head_cell {
  vertical-align: middle;
  font-size: 0.75em;
  font-weight: 700;
  text-align: center;
  height: 100%;
  height: var(--rdp-cell-size);
  padding: 0;
  text-transform: uppercase;
}

.sdk .rdp-tbody {
  border: 0;
}

.sdk .rdp-tfoot {
  margin: 0.5em;
}

.sdk .rdp-cell {
  width: var(--rdp-cell-size);
  height: 100%;
  height: var(--rdp-cell-size);
  padding: 0;
  text-align: center;
}

.sdk .rdp-weeknumber {
  font-size: 0.75em;
}

.sdk .rdp-weeknumber,
.sdk .rdp-day {
  display: flex;
  overflow: hidden;
  align-items: center;
  justify-content: center;
  box-sizing: border-box;
  width: var(--rdp-cell-size);
  max-width: var(--rdp-cell-size);
  height: var(--rdp-cell-size);
  margin: 0;
  border: 2px solid transparent;
  border-radius: 100%;
}

.sdk .rdp-day_today:not(.rdp-day_outside) {
  font-weight: bold;
}

.sdk .rdp-day_selected,
.sdk .rdp-day_selected:focus-visible,
.sdk .rdp-day_selected:hover {
  color: var(--rdp-selected-color);
  opacity: 1;
  background-color: var(--rdp-accent-color);
}

.sdk .rdp-day_outside {
  opacity: 0.5;
}

.sdk .rdp-day_selected:focus-visible {
  /* Since the background is the same use again the outline */
  outline: var(--rdp-outline);
  outline-offset: 2px;
  z-index: 1;
}

.sdk .rdp:not([dir='rtl']) .rdp-day_range_start:not(.rdp-day_range_end) {
  border-top-right-radius: 0;
  border-bottom-right-radius: 0;
}

.sdk .rdp:not([dir='rtl']) .rdp-day_range_end:not(.rdp-day_range_start) {
  border-top-left-radius: 0;
  border-bottom-left-radius: 0;
}

.sdk .rdp[dir='rtl'] .rdp-day_range_start:not(.rdp-day_range_end) {
  border-top-left-radius: 0;
  border-bottom-left-radius: 0;
}

.sdk .rdp[dir='rtl'] .rdp-day_range_end:not(.rdp-day_range_start) {
  border-top-right-radius: 0;
  border-bottom-right-radius: 0;
}

.sdk .rdp-day_range_end.rdp-day_range_start {
  border-radius: 100%;
}

.sdk .rdp-day_range_middle {
  border-radius: 0;
}</style><style type="text/css">[vaul-drawer]{touch-action:none;transition:transform .5s cubic-bezier(.32,.72,0,1)}[vaul-drawer][vaul-drawer-direction=bottom]{transform:translate3d(0,100%,0)}[vaul-drawer][vaul-drawer-direction=top]{transform:translate3d(0,-100%,0)}[vaul-drawer][vaul-drawer-direction=left]{transform:translate3d(-100%,0,0)}[vaul-drawer][vaul-drawer-direction=right]{transform:translate3d(100%,0,0)}.vaul-dragging .vaul-scrollable [vault-drawer-direction=top],.vaul-dragging .vaul-scrollable [vault-drawer-direction=bottom]{overflow-y:hidden!important}.vaul-dragging .vaul-scrollable [vault-drawer-direction=left],.vaul-dragging .vaul-scrollable [vault-drawer-direction=right]{overflow-x:hidden!important}[vaul-drawer][vaul-drawer-visible=true][vaul-drawer-direction=top],[vaul-drawer][vaul-drawer-visible=true][vaul-drawer-direction=bottom]{transform:translate3d(0,var(--snap-point-height, 0),0)}[vaul-drawer][vaul-drawer-visible=true][vaul-drawer-direction=left],[vaul-drawer][vaul-drawer-visible=true][vaul-drawer-direction=right]{transform:translate3d(var(--snap-point-height, 0),0,0)}[vaul-overlay]{opacity:0;transition:opacity .5s cubic-bezier(.32,.72,0,1)}[vaul-overlay][vaul-drawer-visible=true]{opacity:1}[vaul-drawer]:after{content:"";position:absolute;background:inherit;background-color:inherit}[vaul-drawer][vaul-drawer-direction=top]:after{top:initial;bottom:100%;left:0;right:0;height:200%}[vaul-drawer][vaul-drawer-direction=bottom]:after{top:100%;bottom:initial;left:0;right:0;height:200%}[vaul-drawer][vaul-drawer-direction=left]:after{left:initial;right:100%;top:0;bottom:0;width:200%}[vaul-drawer][vaul-drawer-direction=right]:after{left:100%;right:initial;top:0;bottom:0;width:200%}[vaul-overlay][vaul-snap-points=true]:not([vaul-snap-points-overlay="true"]):not([data-state="closed"]){opacity:0}[vaul-overlay][vaul-snap-points-overlay=true]:not([vaul-drawer-visible="false"]){opacity:1}@keyframes fake-animation{}@media (hover: hover) and (pointer: fine){[vaul-drawer]{user-select:none}}
</style><style type="text/css">html[dir=ltr],[data-sonner-toaster][dir=ltr]{--toast-icon-margin-start: -3px;--toast-icon-margin-end: 4px;--toast-svg-margin-start: -1px;--toast-svg-margin-end: 0px;--toast-button-margin-start: auto;--toast-button-margin-end: 0;--toast-close-button-start: 0;--toast-close-button-end: unset;--toast-close-button-transform: translate(-35%, -35%)}html[dir=rtl],[data-sonner-toaster][dir=rtl]{--toast-icon-margin-start: 4px;--toast-icon-margin-end: -3px;--toast-svg-margin-start: 0px;--toast-svg-margin-end: -1px;--toast-button-margin-start: 0;--toast-button-margin-end: auto;--toast-close-button-start: unset;--toast-close-button-end: 0;--toast-close-button-transform: translate(35%, -35%)}[data-sonner-toaster]{position:fixed;width:var(--width);font-family:ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica Neue,Arial,Noto Sans,sans-serif,Apple Color Emoji,Segoe UI Emoji,Segoe UI Symbol,Noto Color Emoji;--gray1: hsl(0, 0%, 99%);--gray2: hsl(0, 0%, 97.3%);--gray3: hsl(0, 0%, 95.1%);--gray4: hsl(0, 0%, 93%);--gray5: hsl(0, 0%, 90.9%);--gray6: hsl(0, 0%, 88.7%);--gray7: hsl(0, 0%, 85.8%);--gray8: hsl(0, 0%, 78%);--gray9: hsl(0, 0%, 56.1%);--gray10: hsl(0, 0%, 52.3%);--gray11: hsl(0, 0%, 43.5%);--gray12: hsl(0, 0%, 9%);--border-radius: 8px;box-sizing:border-box;padding:0;margin:0;list-style:none;outline:none;z-index:999999999}[data-sonner-toaster][data-x-position=right]{right:max(var(--offset),env(safe-area-inset-right))}[data-sonner-toaster][data-x-position=left]{left:max(var(--offset),env(safe-area-inset-left))}[data-sonner-toaster][data-x-position=center]{left:50%;transform:translate(-50%)}[data-sonner-toaster][data-y-position=top]{top:max(var(--offset),env(safe-area-inset-top))}[data-sonner-toaster][data-y-position=bottom]{bottom:max(var(--offset),env(safe-area-inset-bottom))}[data-sonner-toast]{--y: translateY(100%);--lift-amount: calc(var(--lift) * var(--gap));z-index:var(--z-index);position:absolute;opacity:0;transform:var(--y);touch-action:none;will-change:transform,opacity,height;transition:transform .4s,opacity .4s,height .4s,box-shadow .2s;box-sizing:border-box;outline:none;overflow-wrap:anywhere}[data-sonner-toast][data-styled=true]{padding:16px;background:var(--normal-bg);border:1px solid var(--normal-border);color:var(--normal-text);border-radius:var(--border-radius);box-shadow:0 4px 12px #0000001a;width:var(--width);font-size:13px;display:flex;align-items:center;gap:6px}[data-sonner-toast]:focus-visible{box-shadow:0 4px 12px #0000001a,0 0 0 2px #0003}[data-sonner-toast][data-y-position=top]{top:0;--y: translateY(-100%);--lift: 1;--lift-amount: calc(1 * var(--gap))}[data-sonner-toast][data-y-position=bottom]{bottom:0;--y: translateY(100%);--lift: -1;--lift-amount: calc(var(--lift) * var(--gap))}[data-sonner-toast] [data-description]{font-weight:400;line-height:1.4;color:inherit}[data-sonner-toast] [data-title]{font-weight:500;line-height:1.5;color:inherit}[data-sonner-toast] [data-icon]{display:flex;height:16px;width:16px;position:relative;justify-content:flex-start;align-items:center;flex-shrink:0;margin-left:var(--toast-icon-margin-start);margin-right:var(--toast-icon-margin-end)}[data-sonner-toast][data-promise=true] [data-icon]>svg{opacity:0;transform:scale(.8);transform-origin:center;animation:sonner-fade-in .3s ease forwards}[data-sonner-toast] [data-icon]>*{flex-shrink:0}[data-sonner-toast] [data-icon] svg{margin-left:var(--toast-svg-margin-start);margin-right:var(--toast-svg-margin-end)}[data-sonner-toast] [data-content]{display:flex;flex-direction:column;gap:2px}[data-sonner-toast] [data-button]{border-radius:4px;padding-left:8px;padding-right:8px;height:24px;font-size:12px;color:var(--normal-bg);background:var(--normal-text);margin-left:var(--toast-button-margin-start);margin-right:var(--toast-button-margin-end);border:none;cursor:pointer;outline:none;display:flex;align-items:center;flex-shrink:0;transition:opacity .4s,box-shadow .2s}[data-sonner-toast] [data-button]:focus-visible{box-shadow:0 0 0 2px #0006}[data-sonner-toast] [data-button]:first-of-type{margin-left:var(--toast-button-margin-start);margin-right:var(--toast-button-margin-end)}[data-sonner-toast] [data-cancel]{color:var(--normal-text);background:rgba(0,0,0,.08)}[data-sonner-toast][data-theme=dark] [data-cancel]{background:rgba(255,255,255,.3)}[data-sonner-toast] [data-close-button]{position:absolute;left:var(--toast-close-button-start);right:var(--toast-close-button-end);top:0;height:20px;width:20px;display:flex;justify-content:center;align-items:center;padding:0;background:var(--gray1);color:var(--gray12);border:1px solid var(--gray4);transform:var(--toast-close-button-transform);border-radius:50%;cursor:pointer;z-index:1;transition:opacity .1s,background .2s,border-color .2s}[data-sonner-toast] [data-close-button]:focus-visible{box-shadow:0 4px 12px #0000001a,0 0 0 2px #0003}[data-sonner-toast] [data-disabled=true]{cursor:not-allowed}[data-sonner-toast]:hover [data-close-button]:hover{background:var(--gray2);border-color:var(--gray5)}[data-sonner-toast][data-swiping=true]:before{content:"";position:absolute;left:0;right:0;height:100%}[data-sonner-toast][data-y-position=top][data-swiping=true]:before{bottom:50%;transform:scaleY(3) translateY(50%)}[data-sonner-toast][data-y-position=bottom][data-swiping=true]:before{top:50%;transform:scaleY(3) translateY(-50%)}[data-sonner-toast][data-swiping=false][data-removed=true]:before{content:"";position:absolute;inset:0;transform:scaleY(2)}[data-sonner-toast]:after{content:"";position:absolute;left:0;height:calc(var(--gap) + 1px);bottom:100%;width:100%}[data-sonner-toast][data-mounted=true]{--y: translateY(0);opacity:1}[data-sonner-toast][data-expanded=false][data-front=false]{--scale: var(--toasts-before) * .05 + 1;--y: translateY(calc(var(--lift-amount) * var(--toasts-before))) scale(calc(-1 * var(--scale)));height:var(--front-toast-height)}[data-sonner-toast]>*{transition:opacity .4s}[data-sonner-toast][data-expanded=false][data-front=false][data-styled=true]>*{opacity:0}[data-sonner-toast][data-visible=false]{opacity:0;pointer-events:none}[data-sonner-toast][data-mounted=true][data-expanded=true]{--y: translateY(calc(var(--lift) * var(--offset)));height:var(--initial-height)}[data-sonner-toast][data-removed=true][data-front=true][data-swipe-out=false]{--y: translateY(calc(var(--lift) * -100%));opacity:0}[data-sonner-toast][data-removed=true][data-front=false][data-swipe-out=false][data-expanded=true]{--y: translateY(calc(var(--lift) * var(--offset) + var(--lift) * -100%));opacity:0}[data-sonner-toast][data-removed=true][data-front=false][data-swipe-out=false][data-expanded=false]{--y: translateY(40%);opacity:0;transition:transform .5s,opacity .2s}[data-sonner-toast][data-removed=true][data-front=false]:before{height:calc(var(--initial-height) + 20%)}[data-sonner-toast][data-swiping=true]{transform:var(--y) translateY(var(--swipe-amount, 0px));transition:none}[data-sonner-toast][data-swipe-out=true][data-y-position=bottom],[data-sonner-toast][data-swipe-out=true][data-y-position=top]{animation:swipe-out .2s ease-out forwards}@keyframes swipe-out{0%{transform:translateY(calc(var(--lift) * var(--offset) + var(--swipe-amount)));opacity:1}to{transform:translateY(calc(var(--lift) * var(--offset) + var(--swipe-amount) + var(--lift) * -100%));opacity:0}}@media (max-width: 600px){[data-sonner-toaster]{position:fixed;--mobile-offset: 16px;right:var(--mobile-offset);left:var(--mobile-offset);width:100%}[data-sonner-toaster] [data-sonner-toast]{left:0;right:0;width:calc(100% - 32px)}[data-sonner-toaster][data-x-position=left]{left:var(--mobile-offset)}[data-sonner-toaster][data-y-position=bottom]{bottom:20px}[data-sonner-toaster][data-y-position=top]{top:20px}[data-sonner-toaster][data-x-position=center]{left:var(--mobile-offset);right:var(--mobile-offset);transform:none}}[data-sonner-toaster][data-theme=light]{--normal-bg: #fff;--normal-border: var(--gray4);--normal-text: var(--gray12);--success-bg: hsl(143, 85%, 96%);--success-border: hsl(145, 92%, 91%);--success-text: hsl(140, 100%, 27%);--info-bg: hsl(208, 100%, 97%);--info-border: hsl(221, 91%, 91%);--info-text: hsl(210, 92%, 45%);--warning-bg: hsl(49, 100%, 97%);--warning-border: hsl(49, 91%, 91%);--warning-text: hsl(31, 92%, 45%);--error-bg: hsl(359, 100%, 97%);--error-border: hsl(359, 100%, 94%);--error-text: hsl(360, 100%, 45%)}[data-sonner-toaster][data-theme=light] [data-sonner-toast][data-invert=true]{--normal-bg: #000;--normal-border: hsl(0, 0%, 20%);--normal-text: var(--gray1)}[data-sonner-toaster][data-theme=dark] [data-sonner-toast][data-invert=true]{--normal-bg: #fff;--normal-border: var(--gray3);--normal-text: var(--gray12)}[data-sonner-toaster][data-theme=dark]{--normal-bg: #000;--normal-border: hsl(0, 0%, 20%);--normal-text: var(--gray1);--success-bg: hsl(150, 100%, 6%);--success-border: hsl(147, 100%, 12%);--success-text: hsl(150, 86%, 65%);--info-bg: hsl(215, 100%, 6%);--info-border: hsl(223, 100%, 12%);--info-text: hsl(216, 87%, 65%);--warning-bg: hsl(64, 100%, 6%);--warning-border: hsl(60, 100%, 12%);--warning-text: hsl(46, 87%, 65%);--error-bg: hsl(358, 76%, 10%);--error-border: hsl(357, 89%, 16%);--error-text: hsl(358, 100%, 81%)}[data-rich-colors=true] [data-sonner-toast][data-type=success],[data-rich-colors=true] [data-sonner-toast][data-type=success] [data-close-button]{background:var(--success-bg);border-color:var(--success-border);color:var(--success-text)}[data-rich-colors=true] [data-sonner-toast][data-type=info],[data-rich-colors=true] [data-sonner-toast][data-type=info] [data-close-button]{background:var(--info-bg);border-color:var(--info-border);color:var(--info-text)}[data-rich-colors=true] [data-sonner-toast][data-type=warning],[data-rich-colors=true] [data-sonner-toast][data-type=warning] [data-close-button]{background:var(--warning-bg);border-color:var(--warning-border);color:var(--warning-text)}[data-rich-colors=true] [data-sonner-toast][data-type=error],[data-rich-colors=true] [data-sonner-toast][data-type=error] [data-close-button]{background:var(--error-bg);border-color:var(--error-border);color:var(--error-text)}.sonner-loading-wrapper{--size: 16px;height:var(--size);width:var(--size);position:absolute;inset:0;z-index:10}.sonner-loading-wrapper[data-visible=false]{transform-origin:center;animation:sonner-fade-out .2s ease forwards}.sonner-spinner{position:relative;top:50%;left:50%;height:var(--size);width:var(--size)}.sonner-loading-bar{animation:sonner-spin 1.2s linear infinite;background:var(--gray11);border-radius:6px;height:8%;left:-10%;position:absolute;top:-3.9%;width:24%}.sonner-loading-bar:nth-child(1){animation-delay:-1.2s;transform:rotate(.0001deg) translate(146%)}.sonner-loading-bar:nth-child(2){animation-delay:-1.1s;transform:rotate(30deg) translate(146%)}.sonner-loading-bar:nth-child(3){animation-delay:-1s;transform:rotate(60deg) translate(146%)}.sonner-loading-bar:nth-child(4){animation-delay:-.9s;transform:rotate(90deg) translate(146%)}.sonner-loading-bar:nth-child(5){animation-delay:-.8s;transform:rotate(120deg) translate(146%)}.sonner-loading-bar:nth-child(6){animation-delay:-.7s;transform:rotate(150deg) translate(146%)}.sonner-loading-bar:nth-child(7){animation-delay:-.6s;transform:rotate(180deg) translate(146%)}.sonner-loading-bar:nth-child(8){animation-delay:-.5s;transform:rotate(210deg) translate(146%)}.sonner-loading-bar:nth-child(9){animation-delay:-.4s;transform:rotate(240deg) translate(146%)}.sonner-loading-bar:nth-child(10){animation-delay:-.3s;transform:rotate(270deg) translate(146%)}.sonner-loading-bar:nth-child(11){animation-delay:-.2s;transform:rotate(300deg) translate(146%)}.sonner-loading-bar:nth-child(12){animation-delay:-.1s;transform:rotate(330deg) translate(146%)}@keyframes sonner-fade-in{0%{opacity:0;transform:scale(.8)}to{opacity:1;transform:scale(1)}}@keyframes sonner-fade-out{0%{opacity:1;transform:scale(1)}to{opacity:0;transform:scale(.8)}}@keyframes sonner-spin{0%{opacity:1}to{opacity:.15}}@media (prefers-reduced-motion){[data-sonner-toast],[data-sonner-toast]>*,.sonner-loading-bar{transition:none!important;animation:none!important}}.loader{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);transform-origin:center;transition:opacity .2s,transform .2s}.loader[data-visible=false]{opacity:0;transform:scale(.8) translate(-50%,-50%)}
</style></head>

  <body class="signed_in env_production notranslate sidebar-collapsed" translate="no" data-theme-suffix="_alx">
      <!-- Google Tag Manager (noscript) -->
  <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-N4C8MF2"
  height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
  <!-- End Google Tag Manager (noscript) -->


      <div data-react-class="header/Header" data-react-props="{&quot;csrfToken&quot;:&quot;R9OHZfu7PiWyUWh6O35bx-UqAih5eNB_q2P8ofrrhuv0mt8lULgDhGNB2OOpB_J6h2_GtslCAkezXnX1tc8fVg&quot;,&quot;ehubHeaderSdkJsUrl&quot;:&quot;https://ehub.alxafrica.com/sdk/sdk_v1.0.0.js&quot;,&quot;logoUrl&quot;:null,&quot;logoutUrl&quot;:&quot;/auth/sign_out&quot;,&quot;logoClickUrl&quot;:&quot;https://ehub.alxafrica.com&quot;,&quot;redirectUrl&quot;:&quot;/auth/sign_in&quot;,&quot;discord&quot;:{&quot;label&quot;:&quot;Discord&quot;,&quot;targetUrl&quot;:&quot;https://discord.com/channels/1232317148131754014&quot;,&quot;linkOpts&quot;:{&quot;target&quot;:&quot;_blank&quot;,&quot;rel&quot;:&quot;noreferrer&quot;}},&quot;user&quot;:{&quot;myProfileUrl&quot;:&quot;/users/my_profile&quot;,&quot;profilePictureUrl&quot;:&quot;https://savanna.alxafrica.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBK1Y3SUE9PSIsImV4cCI6bnVsbCwicHVyIjoiYmxvYl9pZCJ9fQ==--40237b45f4f925ff9f2709c0d9e6084ff1c01603/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdCem9MWm05eWJXRjBTU0lJYW5CbkJqb0dSVlE2RW5KbGMybDZaVjkwYjE5bWFYUmJCMmtCeUdrQnlBPT0iLCJleHAiOm51bGwsInB1ciI6InZhcmlhdGlvbiJ9fQ==--596ca5c9d0091ccfe5374ad3fb3471cc1878f984/opedp.jpg&quot;},&quot;listItems&quot;:[{&quot;label&quot;:&quot;My Planning&quot;,&quot;iconName&quot;:&quot;calendar&quot;,&quot;targetUrl&quot;:&quot;/planning/me&quot;},{&quot;label&quot;:&quot;Projects&quot;,&quot;iconName&quot;:&quot;code-fork&quot;,&quot;targetUrl&quot;:&quot;/projects/current&quot;,&quot;id&quot;:&quot;sidebar-current-projects-item&quot;},{&quot;label&quot;:&quot;Evaluation quizzes&quot;,&quot;iconName&quot;:&quot;question&quot;,&quot;targetUrl&quot;:&quot;/dashboards/my_current_evaluation_quizzes&quot;},{&quot;label&quot;:&quot;My resources&quot;},{&quot;label&quot;:&quot;Curriculums&quot;,&quot;iconName&quot;:&quot;graduation-cap&quot;,&quot;targetUrl&quot;:&quot;/dashboards/my_curriculums&quot;},{&quot;label&quot;:&quot;Concepts&quot;,&quot;iconName&quot;:&quot;file-text&quot;,&quot;targetUrl&quot;:&quot;/concepts&quot;,&quot;id&quot;:&quot;sidebar-concepts-item&quot;},{&quot;label&quot;:&quot;Conference rooms&quot;,&quot;iconName&quot;:&quot;comments&quot;,&quot;targetUrl&quot;:&quot;/dashboards/video_rooms&quot;,&quot;id&quot;:&quot;sidebar-dashboards-video-rooms&quot;},{&quot;label&quot;:&quot;Sandboxes&quot;,&quot;iconName&quot;:&quot;terminal&quot;,&quot;targetUrl&quot;:&quot;/user_containers/current&quot;,&quot;id&quot;:&quot;sidebar-dashboards-my-containers&quot;},{&quot;label&quot;:&quot;Video on demand&quot;,&quot;iconName&quot;:&quot;film&quot;,&quot;targetUrl&quot;:&quot;/dashboards/videos&quot;}]}" data-react-cache-id="header/Header-0"><div class="header d-flex align-items-center bg-white border-bottom position-fixed top-0 w-100" style="background-color: white; border-color: rgb(229, 230, 230); z-index: 1000;"><div class="header-left align-items-center d-flex position-fixed px-2" style="z-index: 2;"><div class="hamburger mb-0 p-2" style="cursor: pointer; font-size: 24px;"><i class="fa-solid fa-fas fa-bars"></i></div><a class="logo-container bg-white p-1" href="https://ehub.alxafrica.com/" target="_blank"><div><span class="d-md-none"><svg fill="none" height="28" viewBox="0 0 56 28" width="56" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_6404_9311)"><path d="M54.5886 18.9338L49.2322 13.6263L54.5914 8.28351L55.0667 7.80962L54.5914 7.33573L51.0032 3.75856L50.5278 3.28467L50.0525 3.75856L44.6933 9.1013L39.3695 3.75856L38.8941 3.28467L38.4161 3.75856L34.8279 7.33573L34.3553 7.80962L34.8279 8.28351L40.1545 13.6263L34.8279 18.9365L34.3525 19.4104L34.8279 19.8843L38.4161 23.4615L38.8914 23.9353L39.3667 23.4615L44.6933 18.1512L50.0552 23.4615L50.5306 23.9353L51.0032 23.4615L54.5914 19.8843L55.0694 19.4077L54.5886 18.9338Z" fill="black"></path><path d="M24.8457 2.9706V28H31.506V0L24.8457 2.9706Z" fill="black"></path><path d="M14.1242 18.0401C14.0669 19.0969 13.5982 20.0896 12.8177 20.807C12.0373 21.5244 11.0069 21.9098 9.94575 21.8812C8.88459 21.8526 7.87653 21.4123 7.13612 20.6539C6.39571 19.8956 5.98141 18.8791 5.98141 17.8208C5.98141 16.7625 6.39571 15.746 7.13612 14.9877C7.87653 14.2293 8.88459 13.789 9.94575 13.7604C11.0069 13.7318 12.0373 14.1172 12.8177 14.8346C13.5982 15.552 14.0669 16.5447 14.1242 17.6014V18.0401ZM14.1242 7.75V8.62466C12.5912 7.95219 10.9141 7.67149 9.24476 7.80797C7.57546 7.94444 5.96664 8.49379 4.56395 9.40628C3.16125 10.3188 2.00896 11.5656 1.21138 13.0339C0.413791 14.5022 -0.00390625 16.1456 -0.00390625 17.8154C-0.00390625 19.4852 0.413791 21.1286 1.21138 22.5969C2.00896 24.0652 3.16125 25.312 4.56395 26.2245C5.96664 27.137 7.57546 27.6863 9.24476 27.8228C10.9141 27.9593 12.5912 27.6786 14.1242 27.0061V27.9918H20.7845V7.75812L14.1242 7.75Z" fill="black"></path></g><defs><clippath id="clip0_6404_9311"><rect fill="white" height="28" width="55.0667"></rect></clippath></defs></svg></span><span class="d-none d-md-inline"><svg fill="none" height="33" viewBox="0 0 182 33" width="182" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_4816_42204)"><path d="M54.5886 20.9338L49.2322 15.6263L54.5914 10.2835L55.0667 9.80962L54.5914 9.33573L51.0032 5.75856L50.5278 5.28467L50.0525 5.75856L44.6933 11.1013L39.3695 5.75856L38.8941 5.28467L38.4161 5.75856L34.8279 9.33573L34.3553 9.80962L34.8279 10.2835L40.1545 15.6263L34.8279 20.9365L34.3525 21.4104L34.8279 21.8843L38.4161 25.4615L38.8914 25.9353L39.3667 25.4615L44.6933 20.1512L50.0552 25.4615L50.5306 25.9353L51.0032 25.4615L54.5914 21.8843L55.0694 21.4077L54.5886 20.9338Z" fill="black"></path><path d="M24.8457 4.9706V30H31.506V2L24.8457 4.9706Z" fill="black"></path><path d="M14.1247 20.0403C14.0674 21.097 13.5986 22.0897 12.8182 22.8071C12.0378 23.5245 11.0074 23.9099 9.94623 23.8813C8.88508 23.8527 7.87702 23.4124 7.13661 22.6541C6.39619 21.8957 5.9819 20.8792 5.9819 19.8209C5.9819 18.7626 6.39619 17.7461 7.13661 16.9878C7.87702 16.2294 8.88508 15.7891 9.94623 15.7605C11.0074 15.7319 12.0378 16.1173 12.8182 16.8347C13.5986 17.5521 14.0674 18.5448 14.1247 19.6016V20.0403ZM14.1247 9.75012V10.6248C12.5916 9.95231 10.9146 9.67161 9.24525 9.80809C7.57595 9.94457 5.96713 10.4939 4.56444 11.4064C3.16174 12.3189 2.00945 13.5657 1.21186 15.034C0.414279 16.5023 -0.00341797 18.1457 -0.00341797 19.8155C-0.00341797 21.4853 0.414279 23.1287 1.21186 24.597C2.00945 26.0653 3.16174 27.3121 4.56444 28.2246C5.96713 29.1371 7.57595 29.6864 9.24525 29.8229C10.9146 29.9594 12.5916 29.6787 14.1247 29.0062V29.9919H20.785V9.75825L14.1247 9.75012Z" fill="black"></path></g><path d="M73.6023 26.5V8.05845H75.7467V24.5575H83.8826V26.5H73.6023ZM92.5484 26.7523C90.5049 26.7523 88.8904 26.13 87.7047 24.8854C86.5274 23.6408 85.9387 21.9127 85.9387 19.7011C85.9387 17.4726 86.4853 15.7025 87.5785 14.3906C88.6801 13.0788 90.156 12.4229 92.006 12.4229C93.7383 12.4229 95.109 12.9947 96.1181 14.1384C97.1273 15.2736 97.6318 16.7747 97.6318 18.6415V19.966H88.1083C88.1503 21.589 88.5582 22.8209 89.3319 23.6619C90.1139 24.5028 91.2113 24.9233 92.6241 24.9233C94.1125 24.9233 95.5842 24.6121 97.039 23.9898V25.8567C96.2989 26.1762 95.5968 26.4033 94.9324 26.5378C94.2765 26.6808 93.4818 26.7523 92.5484 26.7523ZM91.9808 14.1762C90.8708 14.1762 89.9836 14.5378 89.3192 15.261C88.6633 15.9842 88.2765 16.9849 88.1588 18.2631H95.3865C95.3865 16.9429 95.0922 15.9337 94.5036 15.2358C93.9149 14.5294 93.074 14.1762 91.9808 14.1762ZM109.716 26.5L109.3 24.5322H109.199C108.509 25.3984 107.82 25.987 107.13 26.2982C106.449 26.6009 105.595 26.7523 104.569 26.7523C103.199 26.7523 102.122 26.3991 101.34 25.6927C100.567 24.9863 100.18 23.9814 100.18 22.678C100.18 19.8861 102.412 18.4229 106.878 18.2883L109.224 18.2127V17.3549C109.224 16.2701 108.989 15.4712 108.518 14.9583C108.055 14.4369 107.311 14.1762 106.285 14.1762C105.133 14.1762 103.829 14.5294 102.375 15.2358L101.731 13.6338C102.412 13.2638 103.157 12.9737 103.964 12.7634C104.78 12.5532 105.595 12.4481 106.411 12.4481C108.059 12.4481 109.279 12.8139 110.069 13.5455C110.868 14.2771 111.267 15.4502 111.267 17.0648V26.5H109.716ZM104.986 25.0242C106.289 25.0242 107.311 24.6668 108.051 23.952C108.799 23.2372 109.174 22.2365 109.174 20.9499V19.7011L107.08 19.7894C105.415 19.8483 104.212 20.1089 103.472 20.5715C102.74 21.0256 102.375 21.7361 102.375 22.7032C102.375 23.46 102.602 24.0361 103.056 24.4313C103.518 24.8266 104.162 25.0242 104.986 25.0242ZM121.901 12.4229C122.515 12.4229 123.066 12.4733 123.553 12.5742L123.263 14.5168C122.691 14.3906 122.187 14.3276 121.75 14.3276C120.631 14.3276 119.673 14.7817 118.874 15.6899C118.083 16.5981 117.688 17.7291 117.688 19.083V26.5H115.594V12.6751H117.322L117.562 15.2358H117.663C118.176 14.336 118.794 13.6422 119.517 13.1545C120.24 12.6667 121.035 12.4229 121.901 12.4229ZM135.6 26.5V17.5567C135.6 16.4299 135.343 15.589 134.83 15.0339C134.317 14.4789 133.514 14.2014 132.421 14.2014C130.975 14.2014 129.915 14.5925 129.242 15.3745C128.57 16.1566 128.233 17.4474 128.233 19.247V26.5H126.139V12.6751H127.842L128.183 14.5672H128.284C128.713 13.8861 129.314 13.3605 130.087 12.9905C130.861 12.6121 131.723 12.4229 132.673 12.4229C134.338 12.4229 135.591 12.8265 136.432 13.6338C137.273 14.4327 137.694 15.7151 137.694 17.481V26.5H135.6ZM144.101 26.5H142.008V12.6751H144.101V26.5ZM141.831 8.92881C141.831 8.44948 141.949 8.10049 142.184 7.88185C142.42 7.6548 142.714 7.54128 143.067 7.54128C143.404 7.54128 143.694 7.6548 143.938 7.88185C144.181 8.1089 144.303 8.45789 144.303 8.92881C144.303 9.39973 144.181 9.75292 143.938 9.98838C143.694 10.2154 143.404 10.329 143.067 10.329C142.714 10.329 142.42 10.2154 142.184 9.98838C141.949 9.75292 141.831 9.39973 141.831 8.92881ZM158.002 26.5V17.5567C158.002 16.4299 157.746 15.589 157.233 15.0339C156.72 14.4789 155.917 14.2014 154.823 14.2014C153.377 14.2014 152.317 14.5925 151.645 15.3745C150.972 16.1566 150.636 17.4474 150.636 19.247V26.5H148.542V12.6751H150.244L150.585 14.5672H150.686C151.115 13.8861 151.716 13.3605 152.49 12.9905C153.263 12.6121 154.125 12.4229 155.076 12.4229C156.741 12.4229 157.994 12.8265 158.835 13.6338C159.675 14.4327 160.096 15.7151 160.096 17.481V26.5H158.002ZM175.725 12.6751V13.9996L173.164 14.3023C173.399 14.5967 173.61 14.9835 173.795 15.4628C173.98 15.9337 174.072 16.4677 174.072 17.0648C174.072 18.4187 173.61 19.4993 172.685 20.3066C171.76 21.1139 170.49 21.5175 168.875 21.5175C168.463 21.5175 168.076 21.4839 167.715 21.4166C166.823 21.8875 166.378 22.4804 166.378 23.1952C166.378 23.5736 166.533 23.8553 166.844 24.0403C167.156 24.2169 167.69 24.3052 168.446 24.3052H170.893C172.39 24.3052 173.538 24.6205 174.337 25.2512C175.144 25.8819 175.548 26.7985 175.548 28.0011C175.548 29.5315 174.934 30.6962 173.706 31.4951C172.479 32.3024 170.687 32.706 168.333 32.706C166.525 32.706 165.129 32.3697 164.145 31.6969C163.17 31.0242 162.682 30.0739 162.682 28.8462C162.682 28.0053 162.951 27.2779 163.489 26.664C164.027 26.0501 164.784 25.6338 165.76 25.4152C165.406 25.2554 165.108 25.0074 164.864 24.671C164.629 24.3346 164.511 23.9436 164.511 23.4979C164.511 22.9933 164.645 22.5518 164.914 22.1734C165.184 21.795 165.608 21.4292 166.188 21.076C165.474 20.7817 164.889 20.2813 164.435 19.575C163.989 18.8686 163.767 18.0613 163.767 17.1531C163.767 15.6394 164.221 14.4747 165.129 13.659C166.037 12.8349 167.324 12.4229 168.989 12.4229C169.712 12.4229 170.364 12.507 170.944 12.6751H175.725ZM164.7 28.821C164.7 29.5694 165.015 30.137 165.646 30.5238C166.277 30.9107 167.181 31.1041 168.358 31.1041C170.116 31.1041 171.415 30.8392 172.256 30.3094C173.105 29.788 173.53 29.0774 173.53 28.1777C173.53 27.4292 173.299 26.9079 172.836 26.6135C172.374 26.3276 171.503 26.1847 170.225 26.1847H167.715C166.765 26.1847 166.024 26.4117 165.495 26.8658C164.965 27.3199 164.7 27.9716 164.7 28.821ZM165.835 17.1026C165.835 18.0697 166.109 18.8013 166.655 19.2975C167.202 19.7936 167.963 20.0417 168.938 20.0417C170.982 20.0417 172.003 19.0494 172.003 17.0648C172.003 14.9877 170.969 13.9491 168.9 13.9491C167.917 13.9491 167.16 14.214 166.63 14.7438C166.1 15.2736 165.835 16.0599 165.835 17.1026Z" fill="#344054"></path><defs><clippath id="clip0_4816_42204"><rect fill="white" height="28" transform="translate(0 2)" width="55.0667"></rect></clippath></defs></svg></span></div></a></div><div class="header-right d-flex align-items-center flex-grow-1 justify-content-center" style="z-index: 1;"><div class="w-100"><div class="sdk" id="ehub-root"><div id="ehub-sdk"><div class="relative flex gap-3 z-20 justify-between px-4 py-2 xxs:px-6 xxs:py-4 align-middle bg-background dark:shadow-none min-h-[4.5rem] shadow-none"><div></div><nav aria-label="Main" data-orientation="horizontal" dir="ltr" class="relative z-10 flex max-w-max flex-1 items-center justify-center"><div style="position: relative;"><ul data-orientation="horizontal" class="group flex-1 list-none items-center justify-center space-x-1 flex gap-2" dir="ltr"><li class="flex cursor-pointer"><div class="flex gap-1 border border-border rounded-full py-1 px-2 items-center bg-card hover:bg-accent-foreground"><svg width="25" height="25" viewBox="0 0 25 25" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M17.5141 24.7182H7.77218C5.88161 24.7169 4.06882 23.9654 2.73175 22.6288C1.39469 21.2922 0.64261 19.4797 0.640625 17.5891V7.84727C0.643271 5.95713 1.39564 4.14524 2.73263 2.80918C4.06963 1.47312 5.88205 0.722024 7.77218 0.720703H17.5141C19.4035 0.722687 21.2151 1.47416 22.5511 2.81022C23.8872 4.14628 24.6386 5.95779 24.6406 7.84727V17.5891C24.6386 19.4788 23.8873 21.2906 22.5513 22.6271C21.2153 23.9635 19.4038 24.7156 17.5141 24.7182ZM7.77218 3.04377C6.49862 3.04509 5.2776 3.5516 4.37706 4.45214C3.47651 5.35268 2.97001 6.5737 2.96868 7.84727V17.5891C2.96935 18.8631 3.47556 20.0848 4.37617 20.9859C5.27679 21.887 6.49819 22.3938 7.77218 22.3951H17.5141C18.7879 22.3932 20.0089 21.8861 20.9093 20.9852C21.8098 20.0842 22.3162 18.8629 22.3176 17.5891V7.84727C22.3156 6.57391 21.8089 5.35327 20.9085 4.45287C20.0081 3.55247 18.7874 3.04575 17.5141 3.04377H7.77218Z" fill="#f0c24b"></path><path d="M8.7079 9.01635H14.5206C14.873 9.01635 15.211 9.15635 15.4602 9.40557C15.7094 9.65479 15.8495 9.9928 15.8495 10.3452C15.8495 10.6977 15.7094 11.0357 15.4602 11.2849C15.211 11.5341 14.873 11.6741 14.5206 11.6741H13.1492C12.839 11.6883 12.5463 11.8214 12.3318 12.0459C12.1173 12.2704 11.9976 12.5689 11.9976 12.8794C11.9976 13.1899 12.1173 13.4884 12.3318 13.7129C12.5463 13.9373 12.839 14.0705 13.1492 14.0846H14.5206C15.033 14.1197 15.5471 14.049 16.031 13.8771C16.515 13.7051 16.9584 13.4354 17.3338 13.0849C17.7091 12.7343 18.0084 12.3104 18.213 11.8393C18.4177 11.3682 18.5232 10.8601 18.5232 10.3465C18.5232 9.83289 18.4177 9.32478 18.213 8.8537C18.0084 8.38263 17.7091 7.95865 17.3338 7.6081C16.9584 7.25754 16.515 6.9879 16.031 6.81592C15.5471 6.64394 15.033 6.57329 14.5206 6.60835H8.7079C8.38858 6.60835 8.08234 6.7352 7.85655 6.961C7.63075 7.18679 7.50391 7.49303 7.50391 7.81235C7.50391 8.13167 7.63075 8.43791 7.85655 8.6637C8.08234 8.8895 8.38858 9.01635 8.7079 9.01635Z" fill="#f0c24b"></path><path d="M17.1037 16.4195H10.3194C10.167 16.4195 10.0421 16.4195 9.94468 16.4195V12.4878H10.4443C10.4855 12.4894 10.5262 12.4789 10.5616 12.4577C10.5969 12.4365 10.6253 12.4055 10.6434 12.3684C10.6614 12.3313 10.6682 12.2898 10.663 12.2489C10.6578 12.208 10.6408 12.1695 10.6141 12.1381L9.81229 11.2064L8.88306 10.1173C8.86174 10.0933 8.83558 10.0741 8.8063 10.061C8.77702 10.0478 8.7453 10.041 8.71321 10.041C8.68112 10.041 8.64939 10.0478 8.62011 10.061C8.59084 10.0741 8.56467 10.0933 8.54335 10.1173L7.61163 11.2039L6.81229 12.1356C6.78559 12.167 6.7686 12.2055 6.76341 12.2464C6.75822 12.2873 6.76504 12.3288 6.78306 12.3659C6.80107 12.403 6.82948 12.434 6.86484 12.4552C6.90019 12.4764 6.94095 12.4869 6.98215 12.4853H7.54168V16.8941C7.54168 17.616 7.90388 18.8275 10.3244 18.8275H17.1087C17.4189 18.8134 17.7116 18.6802 17.9261 18.4558C18.1406 18.2313 18.2603 17.9327 18.2603 17.6223C18.2603 17.3118 18.1406 17.0133 17.9261 16.7888C17.7116 16.5643 17.4189 16.4311 17.1087 16.417L17.1037 16.4195Z" fill="#f0c24b"></path></svg><span class="font-bold text-sm text-card-foreground">2215</span><span class="hidden md:inline font-bold text-sm text-card-foreground">points</span></div></li><li class="flex"><button id="radix-:r0:-trigger-notifications" data-state="closed" aria-expanded="false" aria-controls="radix-:r0:-content-notifications" data-radix-collection-item=""><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="[&amp;_path]:stroke-current"><path d="M14.9987 19C14.9987 20.6569 13.6556 22 11.9987 22C10.3419 22 8.99874 20.6569 8.99874 19M13.7952 6.23856C14.2307 5.78864 14.4987 5.17562 14.4987 4.5C14.4987 3.11929 13.3795 2 11.9987 2C10.618 2 9.49874 3.11929 9.49874 4.5C9.49874 5.17562 9.76675 5.78864 10.2022 6.23856M17.9987 11.2C17.9987 9.82087 17.3666 8.49823 16.2414 7.52304C15.1162 6.54786 13.59 6 11.9987 6C10.4074 6 8.88132 6.54786 7.7561 7.52304C6.63089 8.49823 5.99874 9.82087 5.99874 11.2C5.99874 13.4818 5.43288 15.1506 4.72681 16.3447C3.92208 17.7056 3.51972 18.3861 3.53561 18.5486C3.55379 18.7346 3.58726 18.7933 3.73808 18.9036C3.86991 19 4.53225 19 5.85693 19H18.1406C19.4652 19 20.1276 19 20.2594 18.9036C20.4102 18.7933 20.4437 18.7346 20.4619 18.5486C20.4778 18.3861 20.0754 17.7056 19.2707 16.3447C18.5646 15.1506 17.9987 13.4818 17.9987 11.2Z" stroke="#344054" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path></svg></button></li><li class="flex"><button id="radix-:r0:-trigger-applications" data-state="closed" aria-expanded="false" aria-controls="radix-:r0:-content-applications" data-radix-collection-item=""><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="[&amp;_path]:stroke-card-foreground"><path d="M12 6C12.5523 6 13 5.55228 13 5C13 4.44772 12.5523 4 12 4C11.4477 4 11 4.44772 11 5C11 5.55228 11.4477 6 12 6Z" stroke="#667085" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path><path d="M12 13C12.5523 13 13 12.5523 13 12C13 11.4477 12.5523 11 12 11C11.4477 11 11 11.4477 11 12C11 12.5523 11.4477 13 12 13Z" stroke="#667085" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path><path d="M12 20C12.5523 20 13 19.5523 13 19C13 18.4477 12.5523 18 12 18C11.4477 18 11 18.4477 11 19C11 19.5523 11.4477 20 12 20Z" stroke="#667085" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path><path d="M19 6C19.5523 6 20 5.55228 20 5C20 4.44772 19.5523 4 19 4C18.4477 4 18 4.44772 18 5C18 5.55228 18.4477 6 19 6Z" stroke="#667085" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path><path d="M19 13C19.5523 13 20 12.5523 20 12C20 11.4477 19.5523 11 19 11C18.4477 11 18 11.4477 18 12C18 12.5523 18.4477 13 19 13Z" stroke="#667085" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path><path d="M19 20C19.5523 20 20 19.5523 20 19C20 18.4477 19.5523 18 19 18C18.4477 18 18 18.4477 18 19C18 19.5523 18.4477 20 19 20Z" stroke="#667085" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path><path d="M5 6C5.55228 6 6 5.55228 6 5C6 4.44772 5.55228 4 5 4C4.44772 4 4 4.44772 4 5C4 5.55228 4.44772 6 5 6Z" stroke="#667085" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path><path d="M5 13C5.55228 13 6 12.5523 6 12C6 11.4477 5.55228 11 5 11C4.44772 11 4 11.4477 4 12C4 12.5523 4.44772 13 5 13Z" stroke="#667085" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path><path d="M5 20C5.55228 20 6 19.5523 6 19C6 18.4477 5.55228 18 5 18C4.44772 18 4 18.4477 4 19C4 19.5523 4.44772 20 5 20Z" stroke="#667085" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path></svg></button></li><li class="flex"><button id="radix-:r0:-trigger-settings" data-state="closed" aria-expanded="false" aria-controls="radix-:r0:-content-settings" data-radix-collection-item=""><span class="relative flex h-10 w-10 shrink-0 overflow-hidden rounded-full"><img class="aspect-square h-full w-full object-cover" src="./robust_division_calculator_files/6746aff1-f990-4b83-bf20-eebcd5273d79.png"></span></button></li></ul></div><div class="absolute right-0 top-full flex justify-center"></div></nav></div></div></div></div></div></div><div class="sidebar navigation bg-white border-end position-fixed overflow-scroll bottom-0 start-0 " id="sidebar" style="background-color: white; border-color: rgb(238, 238, 238);"><ul class="px-2"><li class="d-flex align-items-center"><span><a href="https://savanna.alxafrica.com/" target="_self"><div class="icon "><i aria-hidden="true" class="fa-solid fa-home"></i></div><div class="ps-3 overflow-hidden text-nowrap" style="display: none;">Home</div></a></span></li><li class="d-flex align-items-center"><span><a href="https://savanna.alxafrica.com/planning/me" target="_self"><div class="icon "><i aria-hidden="true" class="fa-solid fa-calendar"></i></div><div class="ps-3 overflow-hidden text-nowrap" style="display: none;">My Planning</div></a></span></li><li class="d-flex align-items-center" id="sidebar-current-projects-item"><span><a href="https://savanna.alxafrica.com/projects/current" target="_self"><div class="icon "><i aria-hidden="true" class="fa-solid fa-code-fork"></i></div><div class="ps-3 overflow-hidden text-nowrap" style="display: none;">Projects</div></a></span></li><li class="d-flex align-items-center"><span><a href="https://savanna.alxafrica.com/dashboards/my_current_evaluation_quizzes" target="_self"><div class="icon "><i aria-hidden="true" class="fa-solid fa-question"></i></div><div class="ps-3 overflow-hidden text-nowrap" style="display: none;">Evaluation quizzes</div></a></span></li><hr title="My resources"><li class="d-flex align-items-center"><span><a href="https://savanna.alxafrica.com/dashboards/my_curriculums" target="_self"><div class="icon "><i aria-hidden="true" class="fa-solid fa-graduation-cap"></i></div><div class="ps-3 overflow-hidden text-nowrap" style="display: none;">Curriculums</div></a></span></li><li class="d-flex align-items-center" id="sidebar-concepts-item"><span><a href="https://savanna.alxafrica.com/concepts" target="_self"><div class="icon "><i aria-hidden="true" class="fa-solid fa-file-text"></i></div><div class="ps-3 overflow-hidden text-nowrap" style="display: none;">Concepts</div></a></span></li><li class="d-flex align-items-center" id="sidebar-dashboards-video-rooms"><span><a href="https://savanna.alxafrica.com/dashboards/video_rooms" target="_self"><div class="icon "><i aria-hidden="true" class="fa-solid fa-comments"></i></div><div class="ps-3 overflow-hidden text-nowrap" style="display: none;">Conference rooms</div></a></span></li><li class="d-flex align-items-center" id="sidebar-dashboards-my-containers"><span><a href="https://savanna.alxafrica.com/user_containers/current" target="_self"><div class="icon "><i aria-hidden="true" class="fa-solid fa-terminal"></i></div><div class="ps-3 overflow-hidden text-nowrap" style="display: none;">Sandboxes</div></a></span></li><li class="d-flex align-items-center"><span><a href="https://savanna.alxafrica.com/dashboards/videos" target="_self"><div class="icon "><i aria-hidden="true" class="fa-solid fa-film"></i></div><div class="ps-3 overflow-hidden text-nowrap" style="display: none;">Video on demand</div></a></span></li><li class="d-flex align-items-center"><span><a href="https://discord.com/channels/1232317148131754014" target="_blank" rel="noreferrer"><div class="icon"><i aria-hidden="true" class="fa-brands fa-discord"></i></div><div class="text-muted flex-grow-1 ps-3 overflow-hidden text-nowrap" style="display: none;">Discord</div></a></span></li><li class="d-flex align-items-center bg-white border-top border-end position-fixed p-2 bottom-0 start-0 mb-0" style="background-color: white; border-color: rgb(238, 238, 238);"><span><a href="https://savanna.alxafrica.com/users/my_profile"><div class="image "><div class="inner" style="background-image: url(&quot;https://savanna.alxafrica.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBK1Y3SUE9PSIsImV4cCI6bnVsbCwicHVyIjoiYmxvYl9pZCJ9fQ==--40237b45f4f925ff9f2709c0d9e6084ff1c01603/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdCem9MWm05eWJXRjBTU0lJYW5CbkJqb0dSVlE2RW5KbGMybDZaVjkwYjE5bWFYUmJCMmtCeUdrQnlBPT0iLCJleHAiOm51bGwsInB1ciI6InZhcmlhdGlvbiJ9fQ==--596ca5c9d0091ccfe5374ad3fb3471cc1878f984/opedp.jpg&quot;);"></div></div><div class="text-muted d-none flex-grow-1 ps-3 overflow-hidden text-nowrap" style="display: none;">My Profile</div></a></span></li></ul></div></div>


    <main class="content" id="content">
        

        <div id="layout-bars">
          
          <div class="px-5 py-3" id="student-switch-curriculum">
  <div class="btn-group">
    <div class="align-items-center d-flex gap-3" aria-expanded="false" data-bs-auto-close="outside" data-bs-toggle="dropdown" type="button">
      <div class="d-flex flex-column" style="line-height: 16px">
        <span class="fs-4 fw-semibold" style="font-size: 15px !important;">
          Back-End Web Development
        </span>
        <span class="fs-sm text-muted">
          Average: <span class="fw-medium">101.05%</span>
        </span>
      </div>

      <div class="d-flex flex-column justify-content-center">
        <span style="margin-bottom: -4px">
          <i aria-hidden="true" class="fa-solid fa-angle-up fa-fw"></i>
        </span>
        <span style="margin-top: -4px">
          <i aria-hidden="true" class="fa-solid fa-angle-down fa-fw"></i>
        </span>
      </div>
</div>
    <ul class="dropdown-menu-400 fs-5 dropdown-menu">
        <li><a class="dropdown-item" href="https://savanna.alxafrica.com/curriculums/52/observe">
          <div class="align-items-center d-flex py-2">
            <div class="d-flex flex-column" style="line-height: 16px">
              <span class="fs-4 fw-medium" style="font-size: 15px !important;">
                Professional Foundations
              </span>
              <span class="text-muted" style="font-size: 14px !important;">
                Average: <span class="fw-medium">0.0%</span>
              </span>
            </div>

          </div>
</a></li>        <li><a class="dropdown-item" href="https://savanna.alxafrica.com/curriculums/70/observe">
          <div class="align-items-center d-flex py-2">
            <div class="d-flex flex-column" style="line-height: 16px">
              <span class="fs-4 fw-medium" style="font-size: 15px !important;">
                Back-End Web Development
              </span>
              <span class="text-muted" style="font-size: 14px !important;">
                Average: <span class="fw-medium">101.05%</span>
              </span>
            </div>

              <span class="fw-semibold text-info" style="margin-left: 42px">
                <i aria-hidden="true" class="fa-solid fa-check"></i>
              </span>
          </div>
</a></li>        <li><a class="dropdown-item" href="https://savanna.alxafrica.com/curriculums/89/observe">
          <div class="align-items-center d-flex py-2">
            <div class="d-flex flex-column" style="line-height: 16px">
              <span class="fs-4 fw-medium" style="font-size: 15px !important;">
                Professional Foundations
              </span>
              <span class="text-muted" style="font-size: 14px !important;">
                Average: <span class="fw-medium">93.2%</span>
              </span>
            </div>

          </div>
</a></li></ul></div></div>

          
          
          
        </div>

      <article class="">

        
  <div class="d-flex flex-wrap">
      <div class="text-end" id="curriculum_navigation_toggle">
        <button type="button" class="btn btn-default" data-bs-toggle="collapse" data-bs-target="#curriculum_navigation_menu" aria-controls="curriculum_navigation_menu" aria-expanded="false">
          Week 6
          <i aria-hidden="true" class="fa-solid fa-bars ms-1"></i>
        </button>
      </div>

      <div class="collapse" id="curriculum_navigation_menu">
        <div class="d-flex flex-column gap-3 p-3">
  <div class="btn-group">
    <button class="align-items-center d-flex justify-content-between text-start btn btn-default dropdown-toggle" style="font-size: 16px; line-height: 24px; white-space: normal;" aria-expanded="false" data-bs-auto-close="outside" data-bs-toggle="dropdown" type="button">Week 6</button>
    <ul class="dropdown-menu">
        <li><a class="py-3 dropdown-item" href="https://savanna.alxafrica.com/concepts/100011?project_id=102645">Week 0</a></li>
        <li><a class="py-3 dropdown-item" href="https://savanna.alxafrica.com/concepts/105036?project_id=102430">Week 1</a></li>
        <li><a class="py-3 dropdown-item" href="https://savanna.alxafrica.com/projects/101197">Week 2</a></li>
        <li><a class="py-3 dropdown-item" href="https://savanna.alxafrica.com/projects/102756">Week 3</a></li>
        <li><a class="py-3 dropdown-item" href="https://savanna.alxafrica.com/projects/100740">Week 4</a></li>
        <li><a class="py-3 dropdown-item" href="https://savanna.alxafrica.com/projects/100741">Week 5</a></li>
        <li><a class="py-3 active dropdown-item" href="https://savanna.alxafrica.com/projects/100760">Week 6</a></li>
</ul></div>
  <div class="accordion" id="accordion-f217c6fcf790330dee51965e788ea03f">
      <div class="accordion-item">
        <h2 class="accordion-header"><button aria-controls="accordion-f217c6fcf790330dee51965e788ea03f-item-9a88abb7160cd60f8c1a4244db64e9f1" aria-expanded="false" class="accordion-button" data-bs-target="#accordion-f217c6fcf790330dee51965e788ea03f-item-9a88abb7160cd60f8c1a4244db64e9f1" data-bs-toggle="collapse" type="button">Programming Paradigms</button></h2>
        <div class="accordion-collapse collapse show" id="accordion-f217c6fcf790330dee51965e788ea03f-item-9a88abb7160cd60f8c1a4244db64e9f1"><div class="accordion-body accordion-body-flush">
          <div class="list-group list-group-flush">
              <a aria-current="false" class="list-group-item list-group-item-action d-flex align-items-baseline justify-content-between " href="https://savanna.alxafrica.com/concepts/103446?project_id=100760">
                <div>
  <i aria-hidden="true" class="fa-regular fa-file-lines me-2 fa-fw"></i>
  <span>Fundamentals of OOP in Python</span>
</div>
    <i aria-hidden="true" class="fa-solid fa-circle-check  text-success fa-fw"></i>

</a>              <a aria-current="false" class="list-group-item list-group-item-action d-flex align-items-baseline justify-content-between " href="https://savanna.alxafrica.com/concepts/103448?project_id=100760">
                <div>
  <i aria-hidden="true" class="fa-regular fa-file-lines me-2 fa-fw"></i>
  <span>Errors and Exception Handling in Python</span>
</div>
    <i aria-hidden="true" class="fa-solid fa-circle-check  text-success fa-fw"></i>

</a>              <a aria-current="false" class="list-group-item list-group-item-action d-flex align-items-baseline justify-content-between " href="https://savanna.alxafrica.com/concepts/103450?project_id=100760">
                <div>
  <i aria-hidden="true" class="fa-regular fa-file-lines me-2 fa-fw"></i>
  <span>Testing Fundamentals in Python</span>
</div>
    <i aria-hidden="true" class="fa-solid fa-circle-check  text-success fa-fw"></i>

</a>              <a aria-current="false" class="list-group-item list-group-item-action d-flex align-items-baseline justify-content-between " href="https://savanna.alxafrica.com/concepts/111945?project_id=100760">
                <div>
  <i aria-hidden="true" class="fa-regular fa-file-lines me-2 fa-fw"></i>
  <span>How Scoring Works</span>
</div>
    <i aria-hidden="true" class="fa-solid fa-circle-check  text-success fa-fw"></i>

</a>              <a aria-current="false" class="list-group-item list-group-item-action d-flex align-items-baseline justify-content-between " href="https://savanna.alxafrica.com/concepts/111449?project_id=100760">
                <div>
  <i aria-hidden="true" class="fa-regular fa-file-lines me-2 fa-fw"></i>
  <span>How PLDs Work (Step-by-Step) - Get it started!</span>
</div>
    <i aria-hidden="true" class="fa-solid fa-circle-check  text-success fa-fw"></i>

</a>              <a aria-current="true" class="list-group-item list-group-item-action d-flex align-items-baseline justify-content-between active" href="https://savanna.alxafrica.com/projects/100760">
                <div>
  <i aria-hidden="true" class="fa-solid fa-list-check me-2 fa-fw"></i>
  <span>Programming Paradigms &amp; Exception handling</span>
</div>
    <i aria-hidden="true" class="fa-regular fa-circle fa-fw"></i>

</a>          </div>
</div></div></div></div></div>

      </div>

    <div class="flex-grow-1" id="curriculum_navigation_content">
      
<div class="project row">
  <div class="col-12 col-xl-10 contains-images">
    <div id="project_id" style="display: none" data-project-id="100760"></div>

    <div class="vstack gap-3">
        <div class="hstack gap-3 justify-content-between">
    <h1 class="m-0">
      Programming Paradigms &amp; Exception handling
      
    </h1>

  </div>

  

  <div data-react-class="projects/ProjectMetadata" data-react-props="{&quot;metadata&quot;:{&quot;weight&quot;:1,&quot;has_ai_grader&quot;:false,&quot;correction&quot;:{&quot;released&quot;:true,&quot;auto_correction_available_at&quot;:&quot;2025-06-09T00:00:00.000+01:00&quot;,&quot;requires_auto_correction&quot;:true,&quot;requires_manual_correction&quot;:false},&quot;bpi&quot;:{&quot;current&quot;:true,&quot;started&quot;:false,&quot;in_second_deadline&quot;:false,&quot;starts_at&quot;:&quot;2025-06-09T00:00:00.000+01:00&quot;,&quot;ends_at&quot;:&quot;2025-06-16T00:00:00.000+01:00&quot;,&quot;second_deadline_at&quot;:&quot;2025-06-21T00:00:00.000+01:00&quot;},&quot;level&quot;:&quot;Novice&quot;}}" data-react-cache-id="projects/ProjectMetadata-0"><ul class="list-group metadata fs-small" id="project-metadata"><li class="list-group-item"><i aria-hidden="true" class="fa-solid fa-turn-up fa-fw"></i> Novice</li><li class="list-group-item"><i aria-hidden="true" class="fa-solid fa-gear fa-fw"></i> Weight: 1</li><li class="list-group-item"><i aria-hidden="true" class="fa-solid fa-calendar fa-fw"></i> Project will start <span><span class="datetime">Jun 9, 2025 12:00 AM</span></span>, must end by <span><span class="datetime">Jun 16, 2025 12:00 AM</span></span></li><li class="list-group-item"><i aria-hidden="true" class="fa-solid fa-check fa-fw"></i> Checker was released at <span><span class="datetime">Jun 9, 2025 12:00 AM</span></span></li><li class="list-group-item"><i aria-hidden="true" class="fa-solid fa-square-check fa-fw"></i> An auto review will be launched at the deadline</li></ul></div>






        
        
        <div class="card mb-3">
  <div class="card-body">
    <p><img src="./robust_division_calculator_files/07bcdeefe0dfd24a285211b1b984e57288cf37ed.jpg" alt="" loading="lazy" style=""></p>

<p>This project introduces you to the fundamental concepts of Object-Oriented Programming (OOP) in Python and Exception Handling. You’ll learn about classes, objects, the benefits of OOP, explore how to handle errors gracefully, and be introduced to the basics of testing.</p>

<h3><strong>Project Objectives:</strong></h3>

<p>By the end of this project, you should be able to:</p>

<ul>
<li> Explain the core concepts of OOP: classes, objects, encapsulation, and abstraction.</li>
<li>Discuss the significance of OOP in software development and its advantages over other programming paradigms. </li>
<li>Define classes and create objects in Python.</li>
<li>Understand the difference between class attributes, instance methods, and the role of the <code>self</code> keyword within classes.</li>
<li>Differentiate between syntax errors and exceptions in Python.</li>
<li>Identify common Python exceptions and understand their causes.</li>
<li>Utilize <code>try</code>, <code>except</code>, <code>else</code>, and <code>finally</code> blocks to handle exceptions effectively.</li>
<li>Raise exceptions using the <code>raise</code> keyword and create custom exceptions for specific errors in your code. </li>
<li>Explain the importance of testing in software development.</li>
<li>Describe different types of testing, with a focus on unit testing.</li>
<li>Write basic unit tests using Python’s <code>unittest</code> module to verify the functionality of your code.</li>
<li>Structure test cases effectively and understand how test runners work.</li>
</ul>

<p>This project equips you with the foundational knowledge of OOP and exception handling in Python. These skills are essential for building well-structured, maintainable, and robust Python applications.</p>

</div></div>
        
          <div class="card" id="project-quiz-questions-title">
    <h5 class="card-header">
      Quiz questions
</h5>
    <div class="card-body">

        <div class="alert alert-info">
          <strong>Great!</strong>
          You've completed the quiz successfully! Keep going!
          <span id="quiz_questions_collapse_toggle">(Show quiz)</span>
        </div>

      <section class="quiz_questions_show_container" style="display: none;">
        <div class="vstack gap-3">

            <div class="quiz_question_item_container" data-role="quiz_question8458" data-position="6">
              
<div class="" id="quiz_question-8458">
    <h5 class="card-title quiz_question">
        
        Question #0
</h5>
    <!-- Quiz question Body -->
    <p>Which of the following statements is true about instance methods in Python?</p>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="8458">
                <li class="">

  <input type="radio" name="8458" id="8458-1717458576324" value="1717458576324" data-quiz-answer-id="1717458576324" data-quiz-question-id="8458" disabled="disabled" checked="checked">
  <label for="8458-1717458576324"><p>They can access and modify the object’s attributes</p>
</label>
</li>

                <li class="">

  <input type="radio" name="8458" id="8458-1717458550057" value="1717458550057" data-quiz-answer-id="1717458550057" data-quiz-question-id="8458" disabled="disabled">
  <label for="8458-1717458550057"><p>They are shared among all instances of a class</p>
</label>
</li>

                <li class="">

  <input type="radio" name="8458" id="8458-1717458563622" value="1717458563622" data-quiz-answer-id="1717458563622" data-quiz-question-id="8458" disabled="disabled">
  <label for="8458-1717458563622"><p>They are defined outside of the class</p>
</label>
</li>

                <li class="">

  <input type="radio" name="8458" id="8458-1717458587052" value="1717458587052" data-quiz-answer-id="1717458587052" data-quiz-question-id="8458" disabled="disabled">
  <label for="8458-1717458587052"><p>They are called without creating an instance of the class</p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->
</div>

            </div>
              <hr>

            <div class="quiz_question_item_container" data-role="quiz_question8454" data-position="2">
              
<div class="" id="quiz_question-8454">
    <h5 class="card-title quiz_question">
        
        Question #1
</h5>
    <!-- Quiz question Body -->
    <p>Which of the following best describes abstraction in OOP?</p>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="8454">
                <li class="">

  <input type="radio" name="8454" id="8454-1717458068886" value="1717458068886" data-quiz-answer-id="1717458068886" data-quiz-question-id="8454" disabled="disabled">
  <label for="8454-1717458068886"><p>Combining data and methods that operate on the data into a single unit</p>
</label>
</li>

                <li class="">

  <input type="radio" name="8454" id="8454-1717458019692" value="1717458019692" data-quiz-answer-id="1717458019692" data-quiz-question-id="8454" disabled="disabled" checked="checked">
  <label for="8454-1717458019692"><p>Hiding the implementation details and showing only the functionality</p>
</label>
</li>

                <li class="">

  <input type="radio" name="8454" id="8454-1717458025641" value="1717458025641" data-quiz-answer-id="1717458025641" data-quiz-question-id="8454" disabled="disabled">
  <label for="8454-1717458025641"><p>The ability to inherit methods and properties from a parent class</p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->
</div>

            </div>
              <hr>

            <div class="quiz_question_item_container" data-role="quiz_question8461" data-position="9">
              
<div class="" id="quiz_question-8461">
    <h5 class="card-title quiz_question">
        
        Question #2
</h5>
    <!-- Quiz question Body -->
    <p>What does the finally block do in a try-except structure?</p>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="8461">
                <li class="">

  <input type="radio" name="8461" id="8461-1717458770818" value="1717458770818" data-quiz-answer-id="1717458770818" data-quiz-question-id="8461" disabled="disabled" checked="checked">
  <label for="8461-1717458770818"><p>Executes regardless of whether an exception was raised or not</p>
</label>
</li>

                <li class="">

  <input type="radio" name="8461" id="8461-1717458732887" value="1717458732887" data-quiz-answer-id="1717458732887" data-quiz-question-id="8461" disabled="disabled">
  <label for="8461-1717458732887"><p>Executes only if an exception is raised</p>
</label>
</li>

                <li class="">

  <input type="radio" name="8461" id="8461-1717458754638" value="1717458754638" data-quiz-answer-id="1717458754638" data-quiz-question-id="8461" disabled="disabled">
  <label for="8461-1717458754638"><p>Executes only if no exceptions are raised</p>
</label>
</li>

                <li class="">

  <input type="radio" name="8461" id="8461-1717458784683" value="1717458784683" data-quiz-answer-id="1717458784683" data-quiz-question-id="8461" disabled="disabled">
  <label for="8461-1717458784683"><p>Raises an exception</p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->
</div>

            </div>
              <hr>

            <div class="quiz_question_item_container" data-role="quiz_question8457" data-position="5">
              
<div class="" id="quiz_question-8457">
    <h5 class="card-title quiz_question">
        
        Question #3
</h5>
    <!-- Quiz question Body -->
    <p>What is the <code>self</code> keyword used for in Python classes?</p>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="8457">
                <li class="">

  <input type="radio" name="8457" id="8457-1717458481354" value="1717458481354" data-quiz-answer-id="1717458481354" data-quiz-question-id="8457" disabled="disabled">
  <label for="8457-1717458481354"><p>To create a new instance of a class</p>
</label>
</li>

                <li class="">

  <input type="radio" name="8457" id="8457-1717458265971" value="1717458265971" data-quiz-answer-id="1717458265971" data-quiz-question-id="8457" disabled="disabled">
  <label for="8457-1717458265971"><p>To define class methods</p>
</label>
</li>

                <li class="">

  <input type="radio" name="8457" id="8457-1717458474595" value="1717458474595" data-quiz-answer-id="1717458474595" data-quiz-question-id="8457" disabled="disabled" checked="checked">
  <label for="8457-1717458474595"><p>To access variables and methods within a class</p>
</label>
</li>

                <li class="">

  <input type="radio" name="8457" id="8457-1717458502591" value="1717458502591" data-quiz-answer-id="1717458502591" data-quiz-question-id="8457" disabled="disabled">
  <label for="8457-1717458502591"><p>To refer to the class itself</p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->
</div>

            </div>
              <hr>

            <div class="quiz_question_item_container" data-role="quiz_question8453" data-position="1">
              
<div class="" id="quiz_question-8453">
    <h5 class="card-title quiz_question">
        
        Question #4
</h5>
    <!-- Quiz question Body -->
    <p>What is encapsulation in OOP?</p>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="8453">
                <li class="">

  <input type="radio" name="8453" id="8453-1717457962818" value="1717457962818" data-quiz-answer-id="1717457962818" data-quiz-question-id="8453" disabled="disabled">
  <label for="8453-1717457962818"><p>The process of combining two classes</p>
</label>
</li>

                <li class="">

  <input type="radio" name="8453" id="8453-1717457914526" value="1717457914526" data-quiz-answer-id="1717457914526" data-quiz-question-id="8453" disabled="disabled">
  <label for="8453-1717457914526"><p>The ability to create new classes from existing ones</p>
</label>
</li>

                <li class="">

  <input type="radio" name="8453" id="8453-1717457945231" value="1717457945231" data-quiz-answer-id="1717457945231" data-quiz-question-id="8453" disabled="disabled" checked="checked">
  <label for="8453-1717457945231"><p>The practice of hiding the internal state and requiring all interaction to be performed through an object’s methods</p>
</label>
</li>

                <li class="">

  <input type="radio" name="8453" id="8453-1717457980936" value="1717457980936" data-quiz-answer-id="1717457980936" data-quiz-question-id="8453" disabled="disabled">
  <label for="8453-1717457980936"><p>The mechanism of code reuse</p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->
</div>

            </div>
              <hr>

            <div class="quiz_question_item_container" data-role="quiz_question8460" data-position="8">
              
<div class="" id="quiz_question-8460">
    <h5 class="card-title quiz_question">
        
        Question #5
</h5>
    <!-- Quiz question Body -->
    <p>Which of the following is a common Python exception?</p>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="8460">
                <li class="">

  <input type="radio" name="8460" id="8460-1717458675708" value="1717458675708" data-quiz-answer-id="1717458675708" data-quiz-question-id="8460" disabled="disabled">
  <label for="8460-1717458675708"><p>NullPointerException</p>
</label>
</li>

                <li class="">

  <input type="radio" name="8460" id="8460-1717458661065" value="1717458661065" data-quiz-answer-id="1717458661065" data-quiz-question-id="8460" disabled="disabled">
  <label for="8460-1717458661065"><p>TypeMismatchError</p>
</label>
</li>

                <li class="">

  <input type="radio" name="8460" id="8460-1717458668697" value="1717458668697" data-quiz-answer-id="1717458668697" data-quiz-question-id="8460" disabled="disabled" checked="checked">
  <label for="8460-1717458668697"><p>ValueError</p>
</label>
</li>

                <li class="">

  <input type="radio" name="8460" id="8460-1717458684514" value="1717458684514" data-quiz-answer-id="1717458684514" data-quiz-question-id="8460" disabled="disabled">
  <label for="8460-1717458684514"><p>MemoryOverflowError</p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->
</div>

            </div>
              <hr>

            <div class="quiz_question_item_container" data-role="quiz_question8455" data-position="3">
              
<div class="" id="quiz_question-8455">
    <h5 class="card-title quiz_question">
        
        Question #6
</h5>
    <!-- Quiz question Body -->
    <p>Why is OOP significant in software development?</p>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="8455">
                <li class="">

  <input type="radio" name="8455" id="8455-1717458137415" value="1717458137415" data-quiz-answer-id="1717458137415" data-quiz-question-id="8455" disabled="disabled">
  <label for="8455-1717458137415"><p>It ensures that code is free of bugs</p>
</label>
</li>

                <li class="">

  <input type="radio" name="8455" id="8455-1717458122970" value="1717458122970" data-quiz-answer-id="1717458122970" data-quiz-question-id="8455" disabled="disabled">
  <label for="8455-1717458122970"><p>It enables developers to create applications that are fast and efficient</p>
</label>
</li>

                <li class="">

  <input type="radio" name="8455" id="8455-1717458133949" value="1717458133949" data-quiz-answer-id="1717458133949" data-quiz-question-id="8455" disabled="disabled" checked="checked">
  <label for="8455-1717458133949"><p>It makes code reusable, modular, and easier to maintain</p>
</label>
</li>

                <li class="">

  <input type="radio" name="8455" id="8455-1717458147285" value="1717458147285" data-quiz-answer-id="1717458147285" data-quiz-question-id="8455" disabled="disabled">
  <label for="8455-1717458147285"><p>It requires fewer lines of code</p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->
</div>

            </div>
              <hr>

            <div class="quiz_question_item_container" data-role="quiz_question8462" data-position="10">
              
<div class="" id="quiz_question-8462">
    <h5 class="card-title quiz_question">
        
        Question #7
</h5>
    <!-- Quiz question Body -->
    <p>How can you create a custom exception in Python?</p>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="8462">
                <li class="">

  <input type="radio" name="8462" id="8462-1717458858358" value="1717458858358" data-quiz-answer-id="1717458858358" data-quiz-question-id="8462" disabled="disabled">
  <label for="8462-1717458858358"><p>By using the raise keyword</p>
</label>
</li>

                <li class="">

  <input type="radio" name="8462" id="8462-1717458821490" value="1717458821490" data-quiz-answer-id="1717458821490" data-quiz-question-id="8462" disabled="disabled">
  <label for="8462-1717458821490"><p>By defining a new function</p>
</label>
</li>

                <li class="">

  <input type="radio" name="8462" id="8462-1717458854396" value="1717458854396" data-quiz-answer-id="1717458854396" data-quiz-question-id="8462" disabled="disabled" checked="checked">
  <label for="8462-1717458854396"><p>By subclassing the Exception class</p>
</label>
</li>

                <li class="">

  <input type="radio" name="8462" id="8462-1717458870275" value="1717458870275" data-quiz-answer-id="1717458870275" data-quiz-question-id="8462" disabled="disabled">
  <label for="8462-1717458870275"><p>By writing an error message in the console</p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->
</div>

            </div>
              <hr>

            <div class="quiz_question_item_container" data-role="quiz_question8459" data-position="7">
              
<div class="" id="quiz_question-8459">
    <h5 class="card-title quiz_question">
        
        Question #8
</h5>
    <!-- Quiz question Body -->
    <p>What is an exception in Python?</p>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="8459">
                <li class="">

  <input type="radio" name="8459" id="8459-1717458629193" value="1717458629193" data-quiz-answer-id="1717458629193" data-quiz-question-id="8459" disabled="disabled">
  <label for="8459-1717458629193"><p>A reserved keyword in Python</p>
</label>
</li>

                <li class="">

  <input type="radio" name="8459" id="8459-1717458608766" value="1717458608766" data-quiz-answer-id="1717458608766" data-quiz-question-id="8459" disabled="disabled">
  <label for="8459-1717458608766"><p>A syntax error that must be fixed before the program can run</p>
</label>
</li>

                <li class="">

  <input type="radio" name="8459" id="8459-1717458618763" value="1717458618763" data-quiz-answer-id="1717458618763" data-quiz-question-id="8459" disabled="disabled" checked="checked">
  <label for="8459-1717458618763"><p>An error that occurs during the execution of a program</p>
</label>
</li>

                <li class="">

  <input type="radio" name="8459" id="8459-1717458638921" value="1717458638921" data-quiz-answer-id="1717458638921" data-quiz-question-id="8459" disabled="disabled">
  <label for="8459-1717458638921"><p>A type of function in Python</p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->
</div>

            </div>
              <hr>

            <div class="quiz_question_item_container" data-role="quiz_question8456" data-position="4">
              
<div class="" id="quiz_question-8456">
    <h5 class="card-title quiz_question">
        
        Question #9
</h5>
    <!-- Quiz question Body -->
    <p>How do you define a class in Python?</p>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="8456">
                <li class="">

  <input type="radio" name="8456" id="8456-1717458210688" value="1717458210688" data-quiz-answer-id="1717458210688" data-quiz-question-id="8456" disabled="disabled">
  <label for="8456-1717458210688"><p><code>object ClassName():</code></p>
</label>
</li>

                <li class="">

  <input type="radio" name="8456" id="8456-1717458178951" value="1717458178951" data-quiz-answer-id="1717458178951" data-quiz-question-id="8456" disabled="disabled" checked="checked">
  <label for="8456-1717458178951"><p><code>class ClassName():</code></p>
</label>
</li>

                <li class="">

  <input type="radio" name="8456" id="8456-1717458193213" value="1717458193213" data-quiz-answer-id="1717458193213" data-quiz-question-id="8456" disabled="disabled">
  <label for="8456-1717458193213"><p><code>def ClassName():</code></p>
</label>
</li>

                <li class="">

  <input type="radio" name="8456" id="8456-1717458223470" value="1717458223470" data-quiz-answer-id="1717458223470" data-quiz-question-id="8456" disabled="disabled">
  <label for="8456-1717458223470"><p><code>new ClassName():</code></p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->
</div>

            </div>
        </div>

      </section>
</div></div>

          
            <h2 class="mt-5">Tasks</h2>

  <div class="vstack gap-5">
      <div data-role="task102780" data-position="1" id="task-num-0">
        <div>
  <span id="user_id" data-id="906777"></span>

  <div class="card task-card" id="task-102780">
    <h5 class="card-header hstack gap-2 justify-content-between"><span>0. Create a Simple Bank Account Class</span>
      <div class="hstack gap-1">
          <span class="badge text-bg-info">
            mandatory
</span>      </div>
</h5>
    <div class="card-body">
      <!-- Progress vs Score -->

      <!-- Task Body -->
      <p><strong>Objective:</strong> Understand the fundamentals of OOP in Python by implementing a <code>BankAccount</code> class that encapsulates banking operations. Use command line arguments to interact with instances of this class.</p>

<h4>Task Description:</h4>

<p>You will create two Python scripts: <code>bank_account.py</code>, which contains the <code>BankAccount</code> class, and <code>main-0.py</code>, which interfaces with the class through command line arguments to perform banking operations.</p>

<h4><code>bank_account.py</code>:</h4>

<ol>
<li><p><strong>Class Definition:</strong></p>

<ul>
<li>Define a class named <code>BankAccount</code>.</li>
<li>Use the <code>__init__</code> method to initialize an <code>account_balance</code> attribute. Optionally, accept an initial balance parameter, defaulting to zero.</li>
</ul></li>
<li><p><strong>Encapsulation and Behaviors:</strong></p>

<ul>
<li>Implement <code>deposit(amount)</code>, <code>withdraw(amount)</code>, and <code>display_balance()</code> methods.</li>
<li><code>deposit</code> should add the specified amount to <code>account_balance</code>.</li>
<li><code>withdraw</code> should deduct the amount from <code>account_balance</code> if funds are sufficient, returning <code>True</code>; otherwise, return <code>False</code> and do not alter the balance.</li>
<li><code>display_balance</code> should print the current balance in a user-friendly format.</li>
</ul></li>
</ol>

<h4><code>main-0.py</code> for Command Line Interaction:</h4>

<p>This script utilizes <code>BankAccount</code> through command line arguments for banking operations.</p>

<pre><code class="python">import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # Example starting balance
    if len(sys.argv) &lt; 2:
        print("Usage: python main.py &lt;command&gt;:&lt;amount&gt;")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
</code></pre>

<h3>Sample Command Line Usage and Expected Outputs:</h3>

<ol>
<li><strong>Deposit:</strong></li>
</ol>

<pre><code class="sh">   python main-0.py deposit:50
</code></pre>

<p>Expected Output: <code>Deposited: $50</code></p>

<ol>
<li><strong>Withdraw with Sufficient Funds:</strong></li>
</ol>

<pre><code class="sh">   python main-0.py withdraw:20
</code></pre>

<p>Expected Output: <code>Withdrew: $20</code></p>

<ol>
<li><strong>Withdraw with Insufficient Funds:</strong></li>
</ol>

<pre><code class="sh">   python main-0.py withdraw:150
</code></pre>

<p>Expected Output: <code>Insufficient funds.</code></p>

<ol>
<li><strong>Display Balance:</strong></li>
</ol>

<pre><code class="sh">   python main-0.py display
</code></pre>

<p>Expected Output: <code>Current Balance: $[amount]</code></p>

<h3>Implementation Notes for you:</h3>

<ul>
<li>Ensure your <code>BankAccount</code> class in <code>bank_account.py</code> correctly implements the specified functionalities and adheres to the principles of encapsulation.</li>
<li>Use <code>main.py</code> to test your <code>BankAccount</code> class by performing various operations. Adjust the initial balance as needed for testing different scenarios.</li>
<li>This task combines learning OOP concepts with practical command line interaction, enhancing your understanding of Python programming.</li>
</ul>

</div>
    <div class="list-group list-group-flush">
        <!-- LTI Resource -->

      <!-- Task Files -->

      <!-- Task URLs -->

      <!-- Github information -->
        <div class="list-group-item">
          <p><strong>Repo:</strong></p>
          <ul>
            <li>GitHub repository: <code>alx_be_python</code></li>
              <li>Directory: <code>programming_paradigm</code></li>
              <li>File: <code>bank_account.py</code></li>
          </ul>
        </div>

      <!-- Self-paced manual review -->
    </div>

    <!-- Footer - Controls -->
    <div class="card-footer">
        <div class="align-items-center d-flex justify-content-between">
          <div>
      
<button data-bs-target="#task-test-correction-102780-correction-modal" data-bs-toggle="modal" data-gtm-custom-event-options="{&quot;taskId&quot;:102780}" data-gtm-custom-event-name="task_checker_modal" data-task-id="102780" type="button" class="btn btn-default btn-sm check-your-task-102780-modal-button" id="task-num-0-check-code-btn">Check submission</button>


    

</div>


          <div>
          </div>
        </div>


</div></div></div>

      </div>
      <div data-role="task102781" data-position="2" id="task-num-1">
        <div>
  <span id="user_id" data-id="906777"></span>

  <div class="card task-card" id="task-102781">
    <h5 class="card-header hstack gap-2 justify-content-between"><span>1. Robust Division Calculator with Command Line Arguments</span>
      <div class="hstack gap-1">
          <span class="badge text-bg-info">
            mandatory
</span>      </div>
</h5>
    <div class="card-body">
      <!-- Progress vs Score -->

      <!-- Task Body -->
      <p><strong>Objective:</strong> Implement a division calculator that robustly handles errors like division by zero and non-numeric inputs using command line arguments.</p>

<h4>Task Description:</h4>

<p>Create two Python scripts: <code>robust_division_calculator.py</code>, which contains the division logic including error handling, and <code>main.py</code>, which interfaces with the user through the command line.</p>

<h4><code>robust_division_calculator.py</code>:</h4>

<p>Define a function <code>safe_divide(numerator, denominator)</code> that performs division, handling potential errors:</p>

<ul>
<li><strong>Division by Zero:</strong> Use a try-except block to catch <code>ZeroDivisionError</code>.</li>
<li><strong>Non-numeric Input:</strong> Attempt to convert arguments to floats. Use a try-except block to catch <code>ValueError</code> for non-numeric inputs.</li>
<li>Return appropriate messages for errors or the result for successful division.</li>
</ul>

<h4><code>main.py</code> for Command Line Interaction:</h4>

<p>This script will import <code>safe_divide</code> from <code>robust_division_calculator.py</code> and use it to divide numbers provided as command line arguments.</p>

<pre><code class="python">import sys
from robust_division_calculator import safe_divide

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py &lt;numerator&gt; &lt;denominator&gt;")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()
</code></pre>

<h3>Expected Behavior:</h3>

<p>The script is executed from the command line with two additional arguments representing the numerator and denominator. Here are sample commands and the expected outputs:</p>

<ul>
<li><strong>Normal Division:</strong></li>
</ul>

<pre><code>  python main.py 10 5
</code></pre>

<p>Expected Output: <code>The result of the division is 2.0</code></p>

<ul>
<li><strong>Division by Zero:</strong></li>
</ul>

<pre><code>  python main.py 10 0
</code></pre>

<p>Expected Output: <code>Error: Cannot divide by zero.</code></p>

<ul>
<li><strong>Invalid Input (Non-numeric):</strong></li>
</ul>

<pre><code>  python main.py ten 5
</code></pre>

<p>Expected Output: <code>Error: Please enter numeric values only.</code></p>

<h3>Implementation Notes for you:</h3>

<ul>
<li>Focus on error handling within <code>safe_divide</code> in <code>robust_division_calculator.py</code>. Ensure you cover the scenarios detailed above.</li>
<li>Test your function using <code>main.py</code> by passing different types of inputs via command line arguments. This method allows you to quickly assess how well your error handling works in various situations.</li>
<li>This task helps you practice writing error-resistant code, a crucial skill in software development.</li>
</ul>

</div>
    <div class="list-group list-group-flush">
        <!-- LTI Resource -->

      <!-- Task Files -->

      <!-- Task URLs -->

      <!-- Github information -->
        <div class="list-group-item">
          <p><strong>Repo:</strong></p>
          <ul>
            <li>GitHub repository: <code>alx_be_python</code></li>
              <li>Directory: <code>programming_paradigm</code></li>
              <li>File: <code>robust_division_calculator.py</code></li>
          </ul>
        </div>

      <!-- Self-paced manual review -->
    </div>

    <!-- Footer - Controls -->
    <div class="card-footer">
        <div class="align-items-center d-flex justify-content-between">
          <div>
      
<button data-bs-target="#task-test-correction-102781-correction-modal" data-bs-toggle="modal" data-gtm-custom-event-options="{&quot;taskId&quot;:102781}" data-gtm-custom-event-name="task_checker_modal" data-task-id="102781" type="button" class="btn btn-default btn-sm check-your-task-102781-modal-button" id="task-num-1-check-code-btn">Check submission</button>


    

</div>


          <div>
          </div>
        </div>


</div></div></div>

      </div>
      <div data-role="task102782" data-position="3" id="task-num-2">
        <div>
  <span id="user_id" data-id="906777"></span>

  <div class="card task-card" id="task-102782">
    <h5 class="card-header hstack gap-2 justify-content-between"><span>2. Writing Unit Tests for a Simple Calculator Class</span>
      <div class="hstack gap-1">
          <span class="badge text-bg-info">
            mandatory
</span>      </div>
</h5>
    <div class="card-body">
      <!-- Progress vs Score -->

      <!-- Task Body -->
      <p><strong>Objective:</strong> Learn the basics of unit testing in Python by writing tests for a provided <code>SimpleCalculator</code> class that supports addition, subtraction, multiplication, and division operations.</p>

<h4>Provided: <code>simple_calculator.py</code></h4>

<p>You’re given a <code>SimpleCalculator</code> class with basic arithmetic operations. Your task is to write unit tests to verify its correctness.</p>

<pre><code class="python"># simple_calculator.py

class SimpleCalculator:
    """A simple calculator class that supports basic arithmetic operations."""

    def add(self, a, b):
        """Return the addition of a and b."""
        return a + b

    def subtract(self, a, b):
        """Return the subtraction of b from a."""
        return a - b

    def multiply(self, a, b):
        """Return the multiplication of a and b."""
        return a * b

    def divide(self, a, b):
        """Return the division of a by b. Returns None if b is zero."""
        if b == 0:
            return None
        return a / b
</code></pre>

<h4>Task: Write Unit Tests in <code>test_simple_calculator.py</code></h4>

<p>Create a <code>test_simple_calculator.py</code> script to define and run unit tests for each method in the <code>SimpleCalculator</code> class. Your tests should cover various scenarios to ensure the class functions correctly.</p>

<h4>Guidelines for Writing Tests:</h4>

<ol>
<li><p><strong>Import the Necessary Modules:</strong></p>

<ul>
<li>Import the <code>unittest</code> module and the <code>SimpleCalculator</code> class from <code>simple_calculator.py</code>.</li>
</ul></li>
<li><p><strong>Define a Test Class:</strong></p>

<ul>
<li>Create a test class that inherits from <code>unittest.TestCase</code>.</li>
</ul></li>
<li><p><strong>Write Test Methods:</strong></p>

<ul>
<li>Write at least one test method for each operation (<code>add</code>, <code>subtract</code>, <code>multiply</code>, <code>divide</code>) provided by the <code>SimpleCalculator</code>.</li>
<li>Include tests for edge cases, such as dividing by zero.</li>
</ul></li>
<li><p><strong>Use Assertions to Verify Results:</strong></p>

<ul>
<li>Utilize <code>self.assertEqual()</code> to check for expected outcomes.</li>
<li>For the <code>divide</code> method, ensure you test both normal operation and division by zero.</li>
</ul></li>
<li><p><strong>Running Your Tests:</strong></p>

<ul>
<li>Run your tests using the command line: <code>python -m unittest test_simple_calculator.py</code>.</li>
</ul></li>
</ol>

<h4>Example Test Method Structure:</h4>

<pre><code class="python">import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        # Add more assertions to thoroughly test the add method.

# Remember to write additional test methods for subtract, multiply, and divide.
</code></pre>

<h3>Note for you:</h3>

<ul>
<li>Your goal is to think like a tester and identify as many relevant test cases as possible for each method.</li>
<li>Pay special attention to potential edge cases, such as division by zero, which could lead to unexpected behaviors if not properly handled.</li>
<li>Writing comprehensive tests not only helps ensure your code is working correctly but also improves your understanding of how the code operates under different conditions.</li>
</ul>

</div>
    <div class="list-group list-group-flush">
        <!-- LTI Resource -->

      <!-- Task Files -->

      <!-- Task URLs -->

      <!-- Github information -->
        <div class="list-group-item">
          <p><strong>Repo:</strong></p>
          <ul>
            <li>GitHub repository: <code>alx_be_python</code></li>
              <li>Directory: <code>programming_paradigm</code></li>
              <li>File: <code>test_simple_calculator.py</code></li>
          </ul>
        </div>

      <!-- Self-paced manual review -->
    </div>

    <!-- Footer - Controls -->
    <div class="card-footer">
        <div class="align-items-center d-flex justify-content-between">
          <div>
      
<button data-bs-target="#task-test-correction-102782-correction-modal" data-bs-toggle="modal" data-gtm-custom-event-options="{&quot;taskId&quot;:102782}" data-gtm-custom-event-name="task_checker_modal" data-task-id="102782" type="button" class="btn btn-default btn-sm check-your-task-102782-modal-button" id="task-num-2-check-code-btn">Check submission</button>


    

</div>


          <div>
          </div>
        </div>


</div></div></div>

      </div>
      <div data-role="task102783" data-position="4" id="task-num-3">
        <div>
  <span id="user_id" data-id="906777"></span>

  <div class="card task-card" id="task-102783">
    <h5 class="card-header hstack gap-2 justify-content-between"><span>3. Implementing Basic OOP for a Library Management System</span>
      <div class="hstack gap-1">
          <span class="badge text-bg-info">
            mandatory
</span>      </div>
</h5>
    <div class="card-body">
      <!-- Progress vs Score -->

      <!-- Task Body -->
      <p><strong>Objective:</strong> Solidify understanding of basic OOP concepts in Python by implementing a system that tracks books in a library, focusing on classes, object instantiation, and method invocation.</p>

<h4>Your Task: <code>library_management.py</code></h4>

<ul>
<li><strong>Implement a <code>Book</code> class</strong> with public attributes <code>title</code> and <code>author</code>, and a private attribute <code>_is_checked_out</code> to track its availability.</li>
<li><strong>Implement a <code>Library</code> class</strong> with a private list <code>_books</code> to store instances of <code>Book</code>. Include methods to <code>add_book</code>, <code>check_out_book(title)</code>, <code>return_book(title)</code>, and <code>list_available_books</code>.</li>
</ul>

<h4>Provided for Testing: <code>main.py</code></h4>

<p>This script demonstrates how to interact with your <code>Book</code> and <code>Library</code> classes. </p>

<pre><code class="python">from library_management import Book, Library

def main():
    # Setup a small library
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))

    # Initial list of available books
    print("Available books after setup:")
    library.list_available_books()

    # Simulate checking out a book
    library.check_out_book("1984")
    print("\nAvailable books after checking out '1984':")
    library.list_available_books()

    # Simulate returning a book
    library.return_book("1984")
    print("\nAvailable books after returning '1984':")
    library.list_available_books()

if __name__ == "__main__":
    main()
</code></pre>

<h3>Expected Outputs for Each Step in <code>main.py</code>:</h3>

<ol>
<li><strong>After Initial Setup:</strong></li>
</ol>

<pre><code>   Available books after setup:
   Brave New World by Aldous Huxley
   1984 by George Orwell
</code></pre>

<ol>
<li><strong>After Checking Out ‘1984’:</strong></li>
</ol>

<pre><code>   Available books after checking out '1984':
   Brave New World by Aldous Huxley
</code></pre>

<ol>
<li><strong>After Returning ‘1984’:</strong></li>
</ol>

<pre><code>   Available books after returning '1984':
   Brave New World by Aldous Huxley
   1984 by George Orwell
</code></pre>

<h4>Note for you:</h4>

<ul>
<li>Your <code>Book</code> class should provide methods to check a book out and return it, affecting its availability.</li>
<li>Your <code>Library</code> class needs to manage a collection of books, including adding new books to the collection, checking a book out (which marks it as unavailable), returning it (making it available again), and listing all available books.</li>
<li>Implementing these functionalities requires careful thought about how objects interact with each other in terms of state and behavior.</li>
<li>Use the provided <code>main.py</code> for testing your implementation. The expected outputs give you a clear indication of how your program should behave if implemented correctly.</li>
</ul>

</div>
    <div class="list-group list-group-flush">
        <!-- LTI Resource -->

      <!-- Task Files -->

      <!-- Task URLs -->

      <!-- Github information -->
        <div class="list-group-item">
          <p><strong>Repo:</strong></p>
          <ul>
            <li>GitHub repository: <code>alx_be_python</code></li>
              <li>Directory: <code>programming_paradigm</code></li>
              <li>File: <code>library_management.py</code></li>
          </ul>
        </div>

      <!-- Self-paced manual review -->
    </div>

    <!-- Footer - Controls -->
    <div class="card-footer">
        <div class="align-items-center d-flex justify-content-between">
          <div>
      
<button data-bs-target="#task-test-correction-102783-correction-modal" data-bs-toggle="modal" data-gtm-custom-event-options="{&quot;taskId&quot;:102783}" data-gtm-custom-event-name="task_checker_modal" data-task-id="102783" type="button" class="btn btn-default btn-sm check-your-task-102783-modal-button" id="task-num-3-check-code-btn">Check submission</button>


    <button class="btn btn-default btn-sm" data-bs-target="#container-specs-modal" data-bs-toggle="modal" data-gtm-custom-event-name="task_sandbox_modal" data-gtm-custom-event-options="{&quot;taskId&quot;:102783}"><i aria-hidden="true" class="fa-solid fa-terminal"></i><span>Get a sandbox</span></button>

</div>


          <div>
          </div>
        </div>


</div></div></div>

      </div>
  </div>




            

    </div>
  </div>
</div>


      <div class="d-flex col-12 col-xl-10 justify-content-between flex-grow-1 flex-wrap px-0 py-3 gap-3 sm-gap">
  <div>
      <a class="btn btn-default text-start white-space-wrap" href="https://savanna.alxafrica.com/concepts/111449?project_id=100760">
        <div class="d-flex align-items-baseline gap-3">
          <i aria-hidden="true" class="fa-solid fa-angles-left"></i>
          <span>Back</span>
        </div>
</a>  </div>
  <div>
  </div>
</div>

    </div>
  </div>


      </article>

        <div class="copyright">Copyright © 2025 ALX, All rights reserved.</div>

    </main>



        

        <script id="cody-snippet">
          window.codySettings = { widget_id: "9993bc72-2258-452b-a4bf-b2fe1ad5e0d7" };
          !function(){var t=window,e=document,a=function(){var t=e.createElement("script");t.type="text/javascript",t.async=!0,t.src="https://trinketsofcody.com/cody-widget.js";var a=e.getElementsByTagName("script")[0];a.parentNode.insertBefore(t,a)};"complete"===document.readyState?a():t.attachEvent?t.attachEvent("onload",a):t.addEventListener("load",a,!1)}();
        </script>
  

<div aria-hidden="true" aria-labelledby="task-test-correction-102780-correction-modal-label" class="modal modal-lg fade student_modal task_correction_modal text-start" id="task-test-correction-102780-correction-modal" tabindex="-1"><div class="modal-dialog"><div class="modal-content"><div class="modal-header"><h1 class="modal-title fs-5" id="task-test-correction-102780-correction-modal-label">0. Create a Simple Bank Account Class</h1><button aria-label="Close" class="btn-close" data-bs-dismiss="modal" type="button"></button></div><div class="modal-body">    <div class="actions">
      <center>
        <div class="alert alert-info d-none"></div>

        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="102780" data-last-request-id="169704064">Request a new review</button>
        <button class="btn btn-secondary close-modal d-none" data-bs-dismiss="modal" type="button">Close</button>

        <div class="spinner" style="display: none;">
          <div class="bounce1"></div>
          <div class="bounce2"></div>
          <div class="bounce3"></div>
        </div>
        <div class="error fw-semibold m-3 text-danger"></div>
        <div class="info fw-semibold m-3"></div>
      </center>
    </div>
    <div class="result"></div>

    <div class="help">
  <button data-task-id="102780">
    <i aria-hidden="true" class="fa-solid fa-circle-info"></i>
  </button>
  <div class="help-container" data-task-id="102780">
    <div class="check-line">
      <div class="check-inline requirement success">
        <i aria-hidden="true" class="fa-solid fa-circle-check fa-fw"></i><span>Requirement success</span>
      </div>
      <div class="check-inline requirement fail">
        <i aria-hidden="true" class="fa-solid fa-circle-xmark fa-fw"></i><span>Requirement fail</span>
      </div>
    </div>
    <div class="check-line">
      <div class="check-inline code success">
        <i aria-hidden="true" class="fa-solid fa-circle-check fa-fw"></i><span>Code success</span>
      </div>
      <div class="check-inline code fail">
        <i aria-hidden="true" class="fa-solid fa-circle-xmark fa-fw"></i><span>Code fail</span>
      </div>
    </div>
    <div class="check-line">
      <div class="check-inline efficiency success">
        <i aria-hidden="true" class="fa-solid fa-circle-check fa-fw"></i><span>Efficiency success</span>
      </div>
      <div class="check-inline efficiency fail">
        <i aria-hidden="true" class="fa-solid fa-circle-xmark fa-fw"></i><span>Efficiency fail</span>
      </div>
    </div>
    <div class="check-line">
      <div class="check-inline answer success">
        <i aria-hidden="true" class="fa-solid fa-circle-check fa-fw"></i><span>Text answer success</span>
      </div>
      <div class="check-inline answer fail">
        <i aria-hidden="true" class="fa-solid fa-circle-xmark fa-fw"></i><span>Text answer fail</span>
      </div>
    </div>
    <div class="check-line">
      <div class="check-inline requirement fail offline">
        <i aria-hidden="true" class="fa-solid fa-circle-xmark fa-fw"></i><span>Skipped - Previous check failed</span>
      </div>
    </div>
  </div>
</div>

</div></div></div></div><div aria-hidden="true" aria-labelledby="task-test-correction-102781-correction-modal-label" class="modal modal-lg fade student_modal task_correction_modal text-start" id="task-test-correction-102781-correction-modal" tabindex="-1"><div class="modal-dialog"><div class="modal-content"><div class="modal-header"><h1 class="modal-title fs-5" id="task-test-correction-102781-correction-modal-label">1. Robust Division Calculator with Command Line Arguments</h1><button aria-label="Close" class="btn-close" data-bs-dismiss="modal" type="button"></button></div><div class="modal-body">    <div class="actions">
      <center>
        <div class="alert alert-info d-none"></div>

        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="102781">Request a new review</button>
        <button class="btn btn-secondary close-modal d-none" data-bs-dismiss="modal" type="button">Close</button>

        <div class="spinner" style="display: none;">
          <div class="bounce1"></div>
          <div class="bounce2"></div>
          <div class="bounce3"></div>
        </div>
        <div class="error fw-semibold m-3 text-danger"></div>
        <div class="info fw-semibold m-3"></div>
      </center>
    </div>
    <div class="result"></div>

    <div class="help">
  <button data-task-id="102781">
    <i aria-hidden="true" class="fa-solid fa-circle-info"></i>
  </button>
  <div class="help-container" data-task-id="102781">
    <div class="check-line">
      <div class="check-inline requirement success">
        <i aria-hidden="true" class="fa-solid fa-circle-check fa-fw"></i><span>Requirement success</span>
      </div>
      <div class="check-inline requirement fail">
        <i aria-hidden="true" class="fa-solid fa-circle-xmark fa-fw"></i><span>Requirement fail</span>
      </div>
    </div>
    <div class="check-line">
      <div class="check-inline code success">
        <i aria-hidden="true" class="fa-solid fa-circle-check fa-fw"></i><span>Code success</span>
      </div>
      <div class="check-inline code fail">
        <i aria-hidden="true" class="fa-solid fa-circle-xmark fa-fw"></i><span>Code fail</span>
      </div>
    </div>
    <div class="check-line">
      <div class="check-inline efficiency success">
        <i aria-hidden="true" class="fa-solid fa-circle-check fa-fw"></i><span>Efficiency success</span>
      </div>
      <div class="check-inline efficiency fail">
        <i aria-hidden="true" class="fa-solid fa-circle-xmark fa-fw"></i><span>Efficiency fail</span>
      </div>
    </div>
    <div class="check-line">
      <div class="check-inline answer success">
        <i aria-hidden="true" class="fa-solid fa-circle-check fa-fw"></i><span>Text answer success</span>
      </div>
      <div class="check-inline answer fail">
        <i aria-hidden="true" class="fa-solid fa-circle-xmark fa-fw"></i><span>Text answer fail</span>
      </div>
    </div>
    <div class="check-line">
      <div class="check-inline requirement fail offline">
        <i aria-hidden="true" class="fa-solid fa-circle-xmark fa-fw"></i><span>Skipped - Previous check failed</span>
      </div>
    </div>
  </div>
</div>

</div></div></div></div><div aria-hidden="true" aria-labelledby="task-test-correction-102782-correction-modal-label" class="modal modal-lg fade student_modal task_correction_modal text-start" id="task-test-correction-102782-correction-modal" tabindex="-1"><div class="modal-dialog"><div class="modal-content"><div class="modal-header"><h1 class="modal-title fs-5" id="task-test-correction-102782-correction-modal-label">2. Writing Unit Tests for a Simple Calculator Class</h1><button aria-label="Close" class="btn-close" data-bs-dismiss="modal" type="button"></button></div><div class="modal-body">    <div class="actions">
      <center>
        <div class="alert alert-info d-none"></div>

        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="102782">Request a new review</button>
        <button class="btn btn-secondary close-modal d-none" data-bs-dismiss="modal" type="button">Close</button>

        <div class="spinner" style="display: none;">
          <div class="bounce1"></div>
          <div class="bounce2"></div>
          <div class="bounce3"></div>
        </div>
        <div class="error fw-semibold m-3 text-danger"></div>
        <div class="info fw-semibold m-3"></div>
      </center>
    </div>
    <div class="result"></div>

    <div class="help">
  <button data-task-id="102782">
    <i aria-hidden="true" class="fa-solid fa-circle-info"></i>
  </button>
  <div class="help-container" data-task-id="102782">
    <div class="check-line">
      <div class="check-inline requirement success">
        <i aria-hidden="true" class="fa-solid fa-circle-check fa-fw"></i><span>Requirement success</span>
      </div>
      <div class="check-inline requirement fail">
        <i aria-hidden="true" class="fa-solid fa-circle-xmark fa-fw"></i><span>Requirement fail</span>
      </div>
    </div>
    <div class="check-line">
      <div class="check-inline code success">
        <i aria-hidden="true" class="fa-solid fa-circle-check fa-fw"></i><span>Code success</span>
      </div>
      <div class="check-inline code fail">
        <i aria-hidden="true" class="fa-solid fa-circle-xmark fa-fw"></i><span>Code fail</span>
      </div>
    </div>
    <div class="check-line">
      <div class="check-inline efficiency success">
        <i aria-hidden="true" class="fa-solid fa-circle-check fa-fw"></i><span>Efficiency success</span>
      </div>
      <div class="check-inline efficiency fail">
        <i aria-hidden="true" class="fa-solid fa-circle-xmark fa-fw"></i><span>Efficiency fail</span>
      </div>
    </div>
    <div class="check-line">
      <div class="check-inline answer success">
        <i aria-hidden="true" class="fa-solid fa-circle-check fa-fw"></i><span>Text answer success</span>
      </div>
      <div class="check-inline answer fail">
        <i aria-hidden="true" class="fa-solid fa-circle-xmark fa-fw"></i><span>Text answer fail</span>
      </div>
    </div>
    <div class="check-line">
      <div class="check-inline requirement fail offline">
        <i aria-hidden="true" class="fa-solid fa-circle-xmark fa-fw"></i><span>Skipped - Previous check failed</span>
      </div>
    </div>
  </div>
</div>

</div></div></div></div><div aria-hidden="true" aria-labelledby="task-test-correction-102783-correction-modal-label" class="modal modal-lg fade student_modal task_correction_modal text-start" id="task-test-correction-102783-correction-modal" tabindex="-1"><div class="modal-dialog"><div class="modal-content"><div class="modal-header"><h1 class="modal-title fs-5" id="task-test-correction-102783-correction-modal-label">3. Implementing Basic OOP for a Library Management System</h1><button aria-label="Close" class="btn-close" data-bs-dismiss="modal" type="button"></button></div><div class="modal-body">    <div class="actions">
      <center>
        <div class="alert alert-info d-none"></div>

        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="102783">Request a new review</button>
        <button class="btn btn-secondary close-modal d-none" data-bs-dismiss="modal" type="button">Close</button>

        <div class="spinner" style="display: none;">
          <div class="bounce1"></div>
          <div class="bounce2"></div>
          <div class="bounce3"></div>
        </div>
        <div class="error fw-semibold m-3 text-danger"></div>
        <div class="info fw-semibold m-3"></div>
      </center>
    </div>
    <div class="result"></div>

    <div class="help">
  <button data-task-id="102783">
    <i aria-hidden="true" class="fa-solid fa-circle-info"></i>
  </button>
  <div class="help-container" data-task-id="102783">
    <div class="check-line">
      <div class="check-inline requirement success">
        <i aria-hidden="true" class="fa-solid fa-circle-check fa-fw"></i><span>Requirement success</span>
      </div>
      <div class="check-inline requirement fail">
        <i aria-hidden="true" class="fa-solid fa-circle-xmark fa-fw"></i><span>Requirement fail</span>
      </div>
    </div>
    <div class="check-line">
      <div class="check-inline code success">
        <i aria-hidden="true" class="fa-solid fa-circle-check fa-fw"></i><span>Code success</span>
      </div>
      <div class="check-inline code fail">
        <i aria-hidden="true" class="fa-solid fa-circle-xmark fa-fw"></i><span>Code fail</span>
      </div>
    </div>
    <div class="check-line">
      <div class="check-inline efficiency success">
        <i aria-hidden="true" class="fa-solid fa-circle-check fa-fw"></i><span>Efficiency success</span>
      </div>
      <div class="check-inline efficiency fail">
        <i aria-hidden="true" class="fa-solid fa-circle-xmark fa-fw"></i><span>Efficiency fail</span>
      </div>
    </div>
    <div class="check-line">
      <div class="check-inline answer success">
        <i aria-hidden="true" class="fa-solid fa-circle-check fa-fw"></i><span>Text answer success</span>
      </div>
      <div class="check-inline answer fail">
        <i aria-hidden="true" class="fa-solid fa-circle-xmark fa-fw"></i><span>Text answer fail</span>
      </div>
    </div>
    <div class="check-line">
      <div class="check-inline requirement fail offline">
        <i aria-hidden="true" class="fa-solid fa-circle-xmark fa-fw"></i><span>Skipped - Previous check failed</span>
      </div>
    </div>
  </div>
</div>

</div></div></div></div><div aria-hidden="true" aria-labelledby="container-specs-modal-label" class="modal modal-lg fade" id="container-specs-modal" tabindex="-1"><div class="modal-dialog modal-dialog-scrollable"><div class="modal-content"><div class="modal-header"><h1 class="modal-title fs-5" id="container-specs-modal-label">Recommended Sandbox</h1><button aria-label="Close" class="btn-close" data-bs-dismiss="modal" type="button"></button></div><div class="modal-body"><div data-react-class="user_containers/ContainerSpecs" data-react-props="{&quot;containerModelName&quot;:&quot;Sandbox&quot;,&quot;containerSpecs&quot;:[{&quot;available&quot;:true,&quot;description&quot;:&quot;\u003cp\u003eBasic Ubuntu 20.04, with vim, emacs, curl, wget and all needed for Foundations\u003c/p\u003e\n&quot;,&quot;id&quot;:39,&quot;name&quot;:&quot;Ubuntu 20.04&quot;,&quot;online&quot;:true,&quot;container&quot;:{&quot;container_id&quot;:&quot;3f71bb1bbe55e221ebc059d5f2929e25c3955912a713103f96671621f6032ad5&quot;,&quot;id&quot;:717576,&quot;restart_uri&quot;:&quot;/user_containers/717576/restart.json&quot;,&quot;status&quot;:&quot;running&quot;,&quot;uri&quot;:&quot;/user_containers/717576.json&quot;,&quot;wake_uri&quot;:&quot;/user_containers/717576/wake.json&quot;,&quot;webterm_uri&quot;:&quot;/user_containers/717576/webterm&quot;,&quot;host&quot;:&quot;3f71bb1bbe55.bba4db86.alx-cod.online&quot;,&quot;password&quot;:&quot;d1c87eccaadf72f8f34f&quot;,&quot;ports&quot;:{&quot;3000&quot;:33380,&quot;443&quot;:33381,&quot;80&quot;:33382,&quot;22&quot;:33383,&quot;3306&quot;:33379,&quot;4000&quot;:33378,&quot;5000&quot;:33377,&quot;5001&quot;:33376,&quot;8000&quot;:33375,&quot;8080&quot;:33374}}}],&quot;containersLimit&quot;:2,&quot;csrfToken&quot;:&quot;zctcF5f1xaR7qXUSFfgrqBe0H7dRh90e_P6t-xzbx1N-ggRXPPb4Baq5xYuHgYIVdfHbKeG9DybkwySvU_9e7g&quot;,&quot;startStatusURI&quot;:&quot;/user_containers/start_status.json&quot;,&quot;startURI&quot;:&quot;/user_containers/start.json&quot;}" data-react-cache-id="user_containers/ContainerSpecs-0"><div><div class="d-flex gap-4 sandboxes-filters"><a class="btn btn-outline-primary text-nowrap"><i aria-hidden="true" class="fa-solid fa-filter me-1"></i><span>Running only</span></a><input class="form-control" placeholder="Search for an image ..." type="search" value="" style="width: 100%;"></div><div class="mt-3"><h3>1 image<small class="ms-2">(1/2 Sandboxes spawned)</small></h3></div><div class="vstack gap-3 mt-3"><div class="card"><div class="card-body border-start border-5 border-success"><div class="hstack align-items-start flex-wrap justify-content-between"><div><h5 class="card-title mb-0"><i aria-hidden="true" class="fa-solid fa-terminal fa-fw text-success"></i><span class="ms-2">Ubuntu 20.04</span></h5><h6 class="card-subtitle mb-0 mt-2 text-muted"><p>Basic Ubuntu 20.04, with vim, emacs, curl, wget and all needed for Foundations</p>
</h6></div><div class="d-flex flex-wrap gap-5"><div class="align-items-center d-flex gap-3"><div><span><span role="button"><button class="btn btn-default">SSH</button></span></span></div><div><span><span role="button"><button class="btn btn-default">SFTP</button></span></span></div><a class="btn btn-webterm" href="https://savanna.alxafrica.com/user_containers/717576/webterm" rel="noreferrer" target="_blank"><i aria-hidden="true" class="fa-solid fa-terminal fa-fw me-1"></i><span>Webterm</span></a></div><span><a class="btn btn-warning "><i aria-hidden="true" class="fa-solid fa-power-off fa-fw me-1"></i><span>Restart</span></a></span><a class="btn btn-danger"><i aria-hidden="true" class="fa-solid fa-trash fa-fw me-1"></i><span>Destroy</span></a></div></div><div class="d-flex flex-wrap gap-5 mt-3"><div class="p-4" style="flex-shrink: 0;"><div class="d-flex flex-column gap-3"><h4 class="mt-0"><i aria-hidden="true" class="fa-solid fa-user text-info"></i><span class="ms-2">Credentials</span></h4><div class="d-flex gap-2"><strong>Host</strong><span><span role="button"><small>3f71bb1bbe55.bba4db86.alx-cod.online</small></span></span></div><div class="d-flex gap-2"><strong>Username</strong><span><span role="button"><small>3f71bb1bbe55</small></span></span></div><div class="d-flex gap-2"><strong>Password</strong><span><span role="button"><small>d1c87eccaadf72f8f34f</small></span></span></div></div></div><div class="p-4" style="flex: 1 1 40%;"><div class="d-flex flex-column gap-3"><h4 class="mt-0"><i aria-hidden="true" class="fa-solid fa-globe text-info"></i><span class="ms-2">Web access</span></h4><div class="align-items-center d-flex flex-wrap gap-2"><a class="btn btn-outline-primary" href="https://3f71bb1bbe55.bba4db86.alx-cod.online/" rel="noreferrer" target="_blank">HTTPS</a><a class="btn btn-outline-primary" href="http://3f71bb1bbe55.bba4db86.alx-cod.online/" rel="noreferrer" target="_blank">HTTP</a><a class="btn btn-default" href="http://3f71bb1bbe55.bba4db86.alx-cod.online:3000/" rel="noreferrer" target="_blank">3000</a><a class="btn btn-default" href="http://3f71bb1bbe55.bba4db86.alx-cod.online:4000/" rel="noreferrer" target="_blank">4000</a><a class="btn btn-default" href="http://3f71bb1bbe55.bba4db86.alx-cod.online:5000/" rel="noreferrer" target="_blank">5000</a><a class="btn btn-default" href="http://3f71bb1bbe55.bba4db86.alx-cod.online:5001/" rel="noreferrer" target="_blank">5001</a><a class="btn btn-default" href="http://3f71bb1bbe55.bba4db86.alx-cod.online:8000/" rel="noreferrer" target="_blank">8000</a><a class="btn btn-default" href="http://3f71bb1bbe55.bba4db86.alx-cod.online:8080/" rel="noreferrer" target="_blank">8080</a></div></div></div><div class="p-4" style="flex: 1 1 35%;"><div class="d-flex flex-column gap-3"><h4 class="mt-0"><i aria-hidden="true" class="fa-solid fa-signs-post text-info"></i><span class="ms-2">Port mapping</span></h4><div class="align-items-center d-flex flex-wrap"><div class="align-items-center text-primary d-flex gap-2" style="padding: 5px 10px;"><strong>SSH</strong><i aria-hidden="true" class="fa-solid fa-arrow-right-long"></i><span>33383</span></div><div class="align-items-center text-primary d-flex gap-2" style="padding: 5px 10px;"><strong>HTTP</strong><i aria-hidden="true" class="fa-solid fa-arrow-right-long"></i><span>33382</span></div><div class="align-items-center text-primary d-flex gap-2" style="padding: 5px 10px;"><strong>HTTPS</strong><i aria-hidden="true" class="fa-solid fa-arrow-right-long"></i><span>33381</span></div><div class="align-items-center  d-flex gap-2" style="padding: 5px 10px;"><strong>3000</strong><i aria-hidden="true" class="fa-solid fa-arrow-right-long"></i><span>33380</span></div><div class="align-items-center text-primary d-flex gap-2" style="padding: 5px 10px;"><strong>MySQL</strong><i aria-hidden="true" class="fa-solid fa-arrow-right-long"></i><span>33379</span></div><div class="align-items-center  d-flex gap-2" style="padding: 5px 10px;"><strong>4000</strong><i aria-hidden="true" class="fa-solid fa-arrow-right-long"></i><span>33378</span></div><div class="align-items-center  d-flex gap-2" style="padding: 5px 10px;"><strong>5000</strong><i aria-hidden="true" class="fa-solid fa-arrow-right-long"></i><span>33377</span></div><div class="align-items-center  d-flex gap-2" style="padding: 5px 10px;"><strong>5001</strong><i aria-hidden="true" class="fa-solid fa-arrow-right-long"></i><span>33376</span></div><div class="align-items-center  d-flex gap-2" style="padding: 5px 10px;"><strong>8000</strong><i aria-hidden="true" class="fa-solid fa-arrow-right-long"></i><span>33375</span></div><div class="align-items-center  d-flex gap-2" style="padding: 5px 10px;"><strong>8080</strong><i aria-hidden="true" class="fa-solid fa-arrow-right-long"></i><span>33374</span></div></div></div></div></div></div></div></div></div></div></div></div></div></div><div aria-hidden="true" aria-labelledby="markdown-guide-modal-label" class="modal modal-lg fade" id="markdown-guide-modal" tabindex="-1"><div class="modal-dialog modal-dialog-scrollable"><div class="modal-content"><div class="modal-header"><h1 class="modal-title fs-5" id="markdown-guide-modal-label">Markdown guide</h1><button aria-label="Close" class="btn-close" data-bs-dismiss="modal" type="button"></button></div><div class="modal-body"><h4>Emphasis</h4>
<pre>**<strong>bold</strong>**
*<em>italics</em>*
~~<strike>strikethrough</strike>~~</pre>
<h4>Headers</h4>
<pre># Big header
## Medium header
### Small header
#### Tiny header</pre>
<h4>Lists</h4>
<pre>* Generic list item
* Generic list item
* Generic list item

1. Numbered list item
2. Numbered list item
3. Numbered list item</pre>
<h4>Links</h4>
<pre>[Text to display](http://www.example.com)</pre>
<h4>Quotes</h4>
<pre>&gt; This is a quote.
&gt; It can span multiple lines!</pre>
<h4>Images</h4>
<p>CSS style available: <code>width, height, opacity</code></p>
<pre>![](http://www.example.com/image.jpg)
![](http://www.example.com/image.jpg | width: 200px)
![](http://www.example.com/image.jpg | height: 124px | width: 80px | opacity: 0.6)
</pre>
<h4>Tables</h4>
<pre>| Column 1 | Column 2 | Column 3 |
| -------- | -------- | -------- |
| John     | Doe      | Male     |
| Mary     | Smith    | Female   |

<em>Or without aligning the columns...</em>

| Column 1 | Column 2 | Column 3 |
| -------- | -------- | -------- |
| John | Doe | Male |
| Mary | Smith | Female |
</pre>
<h4>Displaying code</h4>
<pre>`var example = "hello!";`

<em>Or spanning multiple lines...</em>

```
var example = "hello!";
alert(example);
```</pre>
</div></div></div></div><div id="cody-wrapper"><style>
  #cody-wrapper .cody-launcher {
    position: var(--position) !important;
    left: var(--left) !important;
    right: var(--right) !important;
    bottom: var(--launcher-bottom) !important;
    border-radius: 9999px !important;
    border: 0 !important;
    padding: 0 !important;
    box-sizing: border-box !important;
    z-index: 999999 !important;
    overflow: hidden !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    transition: box-shadow, scale 300ms linear !important;
    animation: cody-launcher-pulse 4s infinite !important;
    background-color: var(--background-color) !important;
    color: var(--text-color) !important;
    cursor: pointer !important;
    --icon-margin: 12px;
    --close-icon-margin: 16px;
  }

    #cody-wrapper {
    --position: fixed;
    --left: unset;
    --right: 20px;
    --launcher-bottom: 20px;
    --frame-bottom: 90px;
    --background-color: #FBD647;
    --text-color: #020617;
    --shadow-color: 251, 214, 71;
  }

  @media screen and (max-width: 512px) {
    #cody-wrapper {
      --left: unset;
      --right: 10px;
    }
  }

  
  #cody-wrapper .cody-launcher:hover {
    scale: 1.1 !important;
  }

  #cody-wrapper .cody-launcher .cody-close-icon {
    display: none !important;
  }

  #cody-wrapper[data-launcher-open] .cody-launcher .cody-icon {
    display: none !important;;
  }

  #cody-wrapper[data-launcher-open] .cody-launcher .cody-close-icon {
    display: block !important;;
  }

  #cody-wrapper .cody-iframe {
    z-index: 99999 !important;
    transition: visibility .5s, opacity .5s linear !important;
    background-color: #fff !important;
    position: fixed !important;
    left: var(--left) !important;
    right: var(--right) !important;
    bottom: var(--frame-bottom) !important;
    height: 75vh !important;
    width: 448px !important;
    border-radius: 10px !important;
    overflow: hidden !important;
    box-shadow: 0 2px 4px rgba(0, 18, 26, .08), 0 3px 12px rgba(0, 18, 26, .16), 0 2px 14px 0 rgba(0, 18, 26, .2) !important;
    border: 0 !important;
    display: none !important;
  }

  @media screen and (max-height: 667px) {
    #cody-wrapper .cody-iframe {
      height: calc(100vh - 110px) !important;
    }
  }

  @media screen and (max-width: 448px) {
    #cody-wrapper .cody-iframe {
      width: calc(100vw - 20px) !important;
    }
  }

  #cody-wrapper[data-launcher-open] .cody-iframe {
    display: block !important;
  }

  @keyframes cody-launcher-pulse {
    0%, 100% {
      box-shadow: 0 0 18px 4px rgba(var(--shadow-color), 0.8);
    }
    50% {
      box-shadow: 0 0 12px 3px rgba(var(--shadow-color), 0.4);
    }
  }
</style>

<button class="cody-launcher" style="width: 56px; height: 56px; font-size: 16px;">
    <svg class="cody-icon" style="aspect-ratio: 1 / 1; width: 100%; height: 100%; margin: var(--icon-margin)" aria-hidden="true" viewBox="5 7 45 45" xml:space="preserve" xmlns="http://www.w3.org/2000/svg">
    <path d="M41.18 17.86a52.75 52.75 0 0 0-19 0c-.54.1-7.9 2.7-7.9 2.7h.01c-2.9 1.01-4.91 3.75-4.91 6.9v4.85c0 2.96 1.78 5.56 4.4 6.7l17.91 8.93v-6.67c3.18 0 6.36-.29 9.5-.86 4.13-.76 7.13-4.36 7.13-8.56v-5.44c-.01-4.19-3.01-7.79-7.14-8.55zm3.47 14c0 2.43-1.74 4.52-4.13 4.95-2.91.53-5.88.8-8.84.8s-5.93-.27-8.84-.8c-2.39-.44-4.13-2.52-4.13-4.95v-5.44c0-2.43 1.74-4.52 4.13-4.95 2.91-.53 5.88-.8 8.84-.8s5.93.27 8.84.8c2.39.44 4.13 2.52 4.13 4.95v5.44z" fill="currentColor"></path>
    <path d="M26.17 32.79c-.84 0-1.53-.68-1.53-1.53v-4.24c0-.84.68-1.53 1.53-1.53s1.53.68 1.53 1.53v4.24c-.01.85-.69 1.53-1.53 1.53zM37.17 32.79c-.84 0-1.53-.68-1.53-1.53v-4.24c0-.84.68-1.53 1.53-1.53s1.53.68 1.53 1.53v4.24c0 .85-.68 1.53-1.53 1.53z" fill="currentColor"></path>
</svg>    <svg style="aspect-ratio: 1/1; width: 100%; height: 100%; margin: var(--close-icon-margin);" class="cody-close-icon" launchercloseicon="chevron-down" aria-hidden="true" viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg">
    <path d="M239 401c9.4 9.4 24.6 9.4 33.9 0L465 209c9.4-9.4 9.4-24.6 0-33.9s-24.6-9.4-33.9 0l-175 175L81 175c-9.4-9.4-24.6-9.4-33.9 0s-9.4 24.6 0 33.9L239 401z" fill="currentColor"></path>
</svg></button></div></body></html>