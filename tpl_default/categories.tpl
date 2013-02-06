<html>
    <head>
        <title>$page_title</title>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <link rel="stylesheet" href="css/homepage.css" type="text/css" />
    </head>
    <body>
	<div id="container">
  	    <div id="box">
                <div id="top">
                    <div id="left"></div>
                    <div id="right"></div>
                </div>

                <div id="cnt">
                    <div id="wrap">
                        <img alt="Tarantasio LOGO" src="images/title.png" />
                        <!--<div id="content">-->
			    <a href="index.html">Home</a>
		            <table id="packages_table">
			    #for $package in $packages
				#set $package_addr = $package + ".html" 
				#set $package_imgs = $package + ".png" 
                                <tr>
                                    <td><img alt="package $package image"
                                        src="images/packages/$package_imgs"
                                        /></td>
                                    <td>
                                        <a href="$package_addr">$package</a>
                                    </td>
                                </tr>
			    #end for
                            </table>
			    <a href="index.html">Home</a>
                            <!--</div>-->
                    </div>
                </div>
                
                <div id="bottom">
                    <div id="left"></div>
                    <div id="right"></div>
                </div>

            </div>

            <div id="footer">
                CopyRight (c) SomeAgents
            </div>
	</div>
    </body>
</html>
