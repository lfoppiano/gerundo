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
                        <img alt="Tarantasio LOGO" src="tpl_default/images/title.png" />
                        #set back_addr=$package.category + ".html"
                        <a href="$back_addr">Back</a><br />

                        <!--<div id="content">-->
                            <p>
                                <b>name:</b> $package.name<br />
                                <b>url:</b> <a href="package.local_file">click here
                                    to download</a><br /> 
                                <b>category:</b> <a href="$back_addr">$package.category</a><br />
                                <b>description:</b> $package.description<br /> 
                                <b>dependency:</b><br />
                                    #if($package.dependency != None)
                                    <ul>
                                        #for $dep in $package.dependency
                                        #set dep_addr=$dep + ".html"
                                        <li><a href="$dep_addr">$dep</a></li>
                                        #end for
                                    </ul>
                                    #end if
                                </li>
                            </p>	
                        <!--</div>-->
                        <a href="index.html">Home</a>
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
