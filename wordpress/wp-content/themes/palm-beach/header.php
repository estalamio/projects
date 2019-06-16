<?php

/**
 * The header for our theme.
 *
 * Displays all of the <head> section and everything up till <div id="content">
 *
 * @package Palm Beach
 */



?><!DOCTYPE html>

<html <?php language_attributes(); ?>>


<head>

    <meta charset="<?php bloginfo( 'charset' ); ?>">

    <meta name="viewport" content="width=device-width, initial-scale=1">
    
    <meta name="author" content="Mihajilo Mrsevic">
    
    <link rel="profile" href="http://gmpg.org/xfn/11">

    <link rel="pingback" href="<?php bloginfo( 'pingback_url' ); ?>">


<script type="text/javascript">
function mrso(){
	$('.widget-area').addClass('container-fluid');
	$('.widget_sow-slider').addClass('col-lg-8');
	$('.rpw_thumbnail').addClass('col-lg-4');
}

</script>
    <?php wp_head(); ?>

</head>


<body <?php body_class(); ?> onload="mrso(); mrso1();">


<div id="page" class="hfeed site">


    <a class="skip-link screen-reader-text" href="#content"><?php esc_html_e( 'Skip to content', 'palm-beach' ); ?></a>


    <div id="header-top" class="header-bar-wrap"><?php do_action( 'palm_beach_header_bar' ); ?></div>


    <header id="masthead" class="site-header clearfix" role="banner">


        <div class="header-main container clearfix">


            <div id="logo" class="site-branding clearfix">


                <?php palm_beach_site_logo(); ?>

                <?php palm_beach_site_title(); ?>

                <?php palm_beach_site_description(); ?>


            </div><!-- .site-branding -->

<nav class="navbar navbar-default" role="navigation">
    <!-- Brand and toggle get grouped for better mobile display -->
    <div class="navbar-header">
      <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#navbar-collapse-1">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      
    </div>
   <a class="navbar-brand" href="">
               <img src="/wordpress/wp-content/themes/palm-beach/images/crvena005.png" width="200px">
            </a>
    <!-- Collect the nav links, forms, and other content for toggling -->
    <div class="collapse navbar-collapse" id="navbar-collapse-1">
     
      <ul class="nav navbar-nav navbar-left">
        <li><a href="#">NASLOVNA</a></li>
        <li><a href="#">SVE</a></li>
        <li><a href="#">MAGAZIN</a></li>
      </ul>
      
    </div><!-- /.navbar-collapse -->
<?php
            wp_nav_menu( array(
                'menu'              => 'primary',
                'theme_location'    => 'primary',
                'depth'             => 2,
                'container'         => 'div',
                'container_class'   => 'collapse navbar-collapse',
        'container_id'      => 'bs-example-navbar-collapse-1',
                'menu_class'        => 'nav navbar-nav',
                'fallback_cb'       => 'wp_bootstrap_navwalker::fallback',
                'walker'            => new BootstrapNavMenuWalker())

            );
        ?>

       
            

            </nav><!-- #main-navigation -->


        </div><!-- .header-main -->


    </header><!-- #masthead -->


    <?php // Display slider or header image on homepage.

    if ( is_home() or is_page_template( 'template-magazine.php' ) or is_page_template( 'template-slider.php' ) ) :


        palm_beach_slider();

        palm_beach_header_image();


    else :


        palm_beach_header_title();


    endif; ?>



    <?php palm_beach_breadcrumbs(); ?>


    <div id="content" class="site-content container clearfix">

