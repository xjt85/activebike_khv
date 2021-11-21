<?php
/**
 * The header for our theme
 *
 * This is the template that displays all of the <head> section and everything up until <div id="content">
 *
 * @link https://developer.wordpress.org/themes/basics/template-files/#template-partials
 *
 * @package ActiveBike_KHV
 */

?>
<!doctype html>
<html <?php language_attributes(); ?>>
<head>
	<meta charset="<?php bloginfo( 'charset' ); ?>">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="profile" href="https://gmpg.org/xfn/11">
	
	<!-- Put this script tag to the <head> of your page -->
	<script type="text/javascript" src="https://vk.com/js/api/openapi.js?169"></script>

	<script type="text/javascript">
	VK.init({apiId: 7852676, onlyWidgets: true});
	</script>

	<?php wp_head(); ?>

	<!-- Global site tag (gtag.js) - Google Analytics -->
	<script async src="https://www.googletagmanager.com/gtag/js?id=G-G9961718N0"></script>
	<script>
	window.dataLayer = window.dataLayer || [];
	function gtag(){dataLayer.push(arguments);}
	gtag('js', new Date());

	gtag('config', 'G-G9961718N0');
	</script>

	<script>
		$(document).ready(function() {

			// $('.activity-descr').slideUp();
			// $('.activity__show-descr').on('click', function() {;
			// 	$('.activity__show-descr').not($(this)).removeClass('active');
			// 	$('.activity__show-descr').not($(this)).siblings('.activity-descr').slideUp();

			// 	$(this).toggleClass('active');
			// 	$(this).siblings('.activity-descr').slideToggle();
			// });

			$(".header-gallery").owlCarousel({
				// nav: true,
				dots: false,
				loop: false,
				mouseDrag: true,
				touchDrag: true,
				responsiveClass: true,
				responsive: {
					0: {
						items: 2,
					},
					400: {
						items: 2,
					},
					500: {
						items: 3,
					},
					600: {
						items: 4,
					},
					1000: {
						items: 7,
					}
				}
			});
			
			$(".li-gallery").owlCarousel({
				nav: true,
				dots: false,
				loop: true,
				mouseDrag: true,
				touchDrag: true,
				items: 1,
				responsiveClass: true,
				responsive: {
					0: {
						nav: false,
						dots: true
					},
					576: {
						nav: true,
						dots: false
					}
				}
			});

		});

	</script>
	
</head>

<body <?php body_class(); ?>>
<?php wp_body_open(); ?>
<div id="page" class="site">
	<!-- <a class="skip-link screen-reader-text" href="#primary"><?php esc_html_e( 'Skip to content', 'activebike_khv' ); ?></a> -->

	<header class="header">
        <div class="header-topline">
            <div class="container">
                <div class="row justify-content-center align-items-center">
                    <div class="col-3 col-md-2">
                        <div class="site-logo-wrapper">
                            <div class="site-logo"></div>
                        </div>
                    </div>
                    <div class="col-9 col-md-10">
                        <div class="header-text">
                            <h1 class="header-text__title">ACTIVE BIKE</h1>
                            <div class="header-text__subtitle"><span class="header-text__t1">Сообщество велосипедистов </span><span class="header-text__t2"> города Хабаровска</span></div>
                        </div>
                    </div>
                    <div class="col-0 col-md-2"></div>
                </div>
            </div>
        </div>
        <!-- <div class="header-gallery owl-carousel">
            <div class="header-gallery__item"><img src="<?php echo get_template_directory_uri() ?>/assets/img/header-gallery/1.jpg" alt="Наши заезды" class="header-gallery__img"></div>
            <div class="header-gallery__item"><img src="<?php echo get_template_directory_uri() ?>/assets/img/header-gallery/2.jpg" alt="Наши заезды" class="header-gallery__img"></div>
            <div class="header-gallery__item"><img src="<?php echo get_template_directory_uri() ?>/assets/img/header-gallery/3.jpg" alt="Наши заезды" class="header-gallery__img"></div>
            <div class="header-gallery__item"><img src="<?php echo get_template_directory_uri() ?>/assets/img/header-gallery/4.jpg" alt="Наши заезды" class="header-gallery__img"></div>
            <div class="header-gallery__item"><img src="<?php echo get_template_directory_uri() ?>/assets/img/header-gallery/5.jpg" alt="Наши заезды" class="header-gallery__img"></div>
            <div class="header-gallery__item"><img src="<?php echo get_template_directory_uri() ?>/assets/img/header-gallery/6.jpg" alt="Наши заезды" class="header-gallery__img"></div>
            <div class="header-gallery__item"><img src="<?php echo get_template_directory_uri() ?>/assets/img/header-gallery/7.jpg" alt="Наши заезды" class="header-gallery__img"></div>
            <div class="header-gallery__item"><img src="<?php echo get_template_directory_uri() ?>/assets/img/header-gallery/8.jpg" alt="Наши заезды" class="header-gallery__img"></div>
        </div> -->
    </header>

	<!--<header id="masthead" class="site-header">
		<div class="site-branding">
			<?php
			the_custom_logo();
			if ( is_front_page() && is_home() ) :
				?>
				<h1 class="site-title"><a href="<?php echo esc_url( home_url( '/' ) ); ?>" rel="home"><?php bloginfo( 'name' ); ?></a></h1>
				<?php
			else :
				?>
				<p class="site-title"><a href="<?php echo esc_url( home_url( '/' ) ); ?>" rel="home"><?php bloginfo( 'name' ); ?></a></p>
				<?php
			endif;
			$activebike_khv_description = get_bloginfo( 'description', 'display' );
			if ( $activebike_khv_description || is_customize_preview() ) :
				?>
				<p class="site-description"><?php echo $activebike_khv_description; // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped ?></p>
			<?php endif; ?>
		</div><!-- .site-branding -->

		<!--<nav id="site-navigation" class="main-navigation">
			<button class="menu-toggle" aria-controls="primary-menu" aria-expanded="false"><?php esc_html_e( 'Primary Menu', 'activebike_khv' ); ?></button>
			<?php
			wp_nav_menu(
				array(
					'theme_location' => 'menu-1',
					'menu_id'        => 'primary-menu',
				)
			);
			?>
		</nav><!-- #site-navigation -->
	<!--</header><!-- #masthead -->
