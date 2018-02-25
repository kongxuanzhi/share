// echoToFile.js - Write in a given file all the parameters passed on the CLI
"use strict";
// var fs = require('fs'),
//     system = require('system');

// if (system.args.length < 3) {
//     console.log("Usage: echoToFile.js DESTINATION_FILE <arguments to echo...>");
//     phantom.exit(1);
// } else {
//     var content = '',
//         f = null,
//         i;
//     for ( i= 2; i < system.args.length; ++i ) {
//         content += system.args[i] + (i === system.args.length-1 ? '' : ' ');
//     }

//     try {
//         fs.write(system.args[1], content, 'w');
//     } catch(e) {
//         console.log(e);
//     }

//     phantom.exit();
// }


// "use strict";
// if ( typeof(phantom) !== "undefined" ) {
//     var page = require('webpage').create();

//     // Route "console.log()" calls from within the Page context to the main Phantom context (i.e. current "this")
//     page.onConsoleMessage = function(msg) {
//         console.log(msg);
//     };

//     page.onAlert = function(msg) {
//         console.log(msg);
//     };

//     console.log("* Script running in the Phantom context.");
//     console.log("* Script will 'inject' itself in a page...");
//     page.open("http://stockpage.10jqka.com.cn/realHead_v2.html#hs_603458", function(status) {
//         if ( status === "success" ) {
//             var title = page.evaluate(function() {
//                 return document.getElementsByClassName('new_detail')[0].innerHTML;
//             });
//             console.log('Page title is ' + title);
//              console.log(page.injectJs("injectme.js") ? "... done injecting itself!" : "... fail! Check the $PWD?!");
//             //  page.render('example1.png');
//         }
//         phantom.exit();
//     });
// } else {
//     alert("* Script running in the Page context.");
// }

       
/*
    Accessing an iframe (different domain) with PhantomJS
    Example by deerme.org
*/

var page = require('webpage').create(), system = require('system'), t, address,title, linkTitle;
// t = Date.now();
address = 'http://localhost:8888/#/'
page.open(address, function (status)
{
    // if (status !== 'success')
    // {
    //         console.log('FAIL to load the address');
    // }
    // else
    // {
    //     // t = (Date.now()) - t;
        title = page.evaluate( function(){
            return document.getElementById("#ifrm");
        });
        linkTitle = page.evaluate( function(){
            // The site contain ing jQuery?
            if ( typeof(jQuery) == "undefined" )
            {
                // Force Load
                page.injectJs('https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js');
            }
            // first iframe #aswift_2
            // second iframe #google_ads_frame3
            return jQuery("#ifrm").contents()
                .find("body").toString();// document.getElementById("#ifrm").innerHTML;
                // .find("new_detail")
        });
    //     console.log('Loading time: ' + t + ' msec');    
        console.log('Webpage title: ' + linkTitle);
    //     console.log('Link title (iframe adsense): ' + linkTitle);
    // }
    console.log(status)
    phantom.exit();
});