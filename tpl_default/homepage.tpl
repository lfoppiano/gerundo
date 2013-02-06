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

                        <div id="header">-
                        <img alt="Tarantasio LOGO" src="images/title.png" />
                        </div>                        
			<div id="content">
				
        	            <table id="category_table">
                                #set $i = 1
                                <tr>
                                #for $category in $categories
                                    <td>
                                        #set category_addr = $category + ".html"
                                        #set category_img = $category + ".png"
                                        <a href="$category_addr">
                                            <img alt="$category image" src="images/categories/$category_img" />
                                        </a><br />
                                        $category
                                    </td>
                                #if $i % $row_num_category == 0
                                </tr><tr>
                                #end if
                                #set $i = $i + 1
                                #end for
                    	    </table>
	                </div>
                    </div>
                    <div id="bottom">
                        <div id="left"></div>
                        <div id="right"></div>
                    </div>
                </div>

            </div>

            <div id="footer">
                CopyRight (c) SomeAgents
            </div>
	</div>
    </body>
</html>
