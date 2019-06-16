<?php
/*
Plugin Name: lwd Popular Posts Widget
Plugin URI: http://smallbizwebdesigns.co.uk
Description: This is a customizable widget which will displays the popular posts on your blog on the based on post views.
Author: londonwebdesign
Version: 1.0
Author URI: http://smallbizwebdesigns.co.uk/
*/
   
//Add style 
function fm_popularposts_styles() {
    wp_enqueue_style( 'fmposts-style', plugins_url( 'css/style.css', __FILE__ ) );
}

add_action( 'wp_enqueue_scripts', 'fm_popularposts_styles' );

// function to set the popular posts
function fm_set_post_views($postID) {
    $count_key = 'fm_post_views_count';
    $count = get_post_meta($postID, $count_key, true);
    if($count==''){
        $count = 0;
        delete_post_meta($postID, $count_key);
        add_post_meta($postID, $count_key, '0');
    }else{
        $count++;
        update_post_meta($postID, $count_key, $count);
    }
}

//To keep the count accurate, lets get rid of prefetching
remove_action( 'wp_head', 'adjacent_posts_rel_link_wp_head', 10, 0);

// track post view
function fm_track_post_views ($post_id) {
    if ( !is_single() ) return;
    if ( empty ( $post_id) ) {
        global $post;
        $post_id = $post->ID;    
    }
    fm_set_post_views($post_id);
}

add_action( 'wp_head', 'fm_track_post_views');


//get the most view's post
function fm_get_post_views($postID){
    $count_key = 'fm_post_views_count';
    $count = get_post_meta($postID, $count_key, true);
    if($count==''){
        delete_post_meta($postID, $count_key);
        add_post_meta($postID, $count_key, '0');
        return "0 View";
    }
    return $count.' Views';
}


//Widgets code start
$theme->options['widgets_options']['lwd'] =  isset($theme->options['widgets_options']['lwd'])
    ? array_merge($themater_lwd_defaults, $theme->options['widgets_options']['lwd'])
    : $themater_lwd_defaults;
        
add_action('widgets_init', create_function('', 'return register_widget("Thematerlwd");'));

class Thematerlwd extends WP_Widget 
{
    function __construct() 
    {
        $widget_options = array('description' => __('lwd Popular Posts Widget will display the post with thumbnail based on views.', 'themater') );
        $control_options = array( 'width' => 440);
		$this->WP_Widget('themater_lwd', '&raquo; lwd Popular Posts Widget', $widget_options, $control_options);
    }

    function widget($args, $instance)
    {
        global $wpdb, $theme;
        extract( $args );
        $title = apply_filters('widget_title', $instance['title']);
        $postupto = $instance['postupto'];
        $show_thumbnail = $instance['show_thumbnail'] == 'true' ? 'true' : 'false';
        $show_views = $instance['show_views'] == 'true' ? 'true' : 'false';
        ?>
        
        <section class="widget">
        <h2 class="widget-title"><?php echo esc_attr($instance['title']); ?></h2>
        <ul class="widget-container">
        <?php
            $popularpost = new WP_Query( 
               array( 'posts_per_page' => $postupto, 
               'meta_key' => 'fm_post_views_count',
               'orderby' => 'meta_value_num',
               'order' => 'DESC')
        );

        while ( $popularpost->have_posts() ) : $popularpost->the_post(); ?>

            <li class="popular-posts-widget">    
            <a href="<?php the_permalink(); ?>"><?php the_post_thumbnail(array('62')); ?></a>
            <a href="<?php the_permalink(); ?>" class="fmpost-title"><?php the_title();?></a>
                <span class="postviews"> <?php global $post;               
                    echo get_post_meta($post->ID, 'fm_post_views_count', true);?> Views</span>
            </li>
            <?php endwhile; ?>
        </ul>
</section>
<?php }

 function update($new_instance, $old_instance) 
    {		
    	$instance = $old_instance;
    	$instance['title'] = strip_tags($new_instance['title']);
        $instance['postupto'] = strip_tags($new_instance['postupto']);
        $instance['show_thumbnail'] = strip_tags($new_instance['show_thumbnail']);
        $instance['show_views'] = strip_tags($new_instance['show_views']);
        return $instance;
    }
    
    function form($instance) 
    {	
        global $theme;
		$instance = wp_parse_args( (array) $instance, $theme->options['widgets_options']['lwd'] );
        
        ?>
        
            <div class="tt-widget">
                <table width="100%">
                    <tr>
                        <td class="tt-widget-label" width="30%"><label for="<?php echo $this->get_field_id('title'); ?>">Title:</label></td>
                        <td class="tt-widget-content" width="70%"><input class="widefat" id="<?php echo $this->get_field_id('title'); ?>" name="<?php echo $this->get_field_name('title'); ?>" type="text" value="<?php echo esc_attr($instance['title']); ?>" /></td>
                    </tr>
                    
                    <tr>
                        <td class="tt-widget-label"><label for="<?php echo $this->get_field_id('url'); ?>">Show posts up to:</label></td>
                        <td class="tt-widget-content"><input class="widefat" id="<?php echo $this->get_field_id('postupto'); ?>" name="<?php echo $this->get_field_name('postupto'); ?>" type="text" value="<?php echo esc_attr($instance['postupto']); ?>" /></td>
                    </tr>
                
                    <tr>
                        <td class="tt-widget-label">Advance Settings:</td>
                        <td class="tt-widget-content">
                            <input type="checkbox" name="<?php echo $this->get_field_name('show_thumbnail'); ?>"  <?php checked('true', $instance['show_thumbnail']); ?> value="true" />  <?php _e('Show Post Thumbnail', 'themater'); ?>
                            <br /><input type="checkbox" name="<?php echo $this->get_field_name('stream'); ?>"  <?php checked('true', $instance['stream']); ?> value="true" />  <?php _e('Show Views', 'themater'); ?>
                        </td>
                    </tr>
                    
                </table>
            </div>
            
        <?php 
    }
} 

?>