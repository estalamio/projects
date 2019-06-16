<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the
 * installation. You don't have to use the web site, you can
 * copy this file to "wp-config.php" and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * MySQL settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://codex.wordpress.org/Editing_wp-config.php
 *
 * @package WordPress
 */

// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define('WP_CACHE', true); //Added by WP-Cache Manager
define( 'WPCACHEHOME', '/home/eubiznis/public_html/wordpress/wp-content/plugins/wp-super-cache/' ); //Added by WP-Cache Manager
define('DB_NAME', 'eubiznis_blog');

/** MySQL database username */
define('DB_USER', 'eubiznis_maja');

/** MySQL database password */
define('DB_PASSWORD', 'MajaKreativniUm');

/** MySQL hostname */
define('DB_HOST', '85.119.156.11');

/** Database Charset to use in creating database tables. */
define('DB_CHARSET', 'utf8mb4');

/** The Database Collate type. Don't change this if in doubt. */
define('DB_COLLATE', '');

/**#@+
 * Authentication Unique Keys and Salts.
 *
 * Change these to different unique phrases!
 * You can generate these using the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}
 * You can change these at any point in time to invalidate all existing cookies. This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define('AUTH_KEY',         ';r.FMJ$;ENNwim:^NtF/pM|%!{_GaRxd./)xZJ8GYifqN2w3yy`:90Hzu MS)65n');
define('SECURE_AUTH_KEY',  '.wJ8b;:]~>WeX7tuoEu*w|0^[3.cixvppQHkIWtf)4{Ti;!/FOJ)WkG)4(y@S9&8');
define('LOGGED_IN_KEY',    'N%^o0} m%.~k+>*}&WKI_44pf!UXVd/JMeG&Q]&@CJebRv-;IEj,yR!HtSZ%^$bD');
define('NONCE_KEY',        '-W!Xu<T[aL9+{C(:d6tAC/78(V!11X=zqs(`%o+Rr{C1M`mia#)<OYK54?0A%fLg');
define('AUTH_SALT',        'Tr_*WM8nSgPD}vs^6=Ui7GJ~3uNFhAZ9fn#lq$ LT2Cb_HQ86<uY nBx|(Au`195');
define('SECURE_AUTH_SALT', '5B7:G+lH}zzG^,+pnz_b/cSFqc e&29HtMb;GO/b5T,^Y6gkz40aLho7W9K}>iS%');
define('LOGGED_IN_SALT',   '[2PR4^j0E}pQN|_eR6bzXmi]Xhx_fx|Y0#M^(;6Z8RhI;frX%)GB6:7aRTc.`vcF');
define('NONCE_SALT',       '?}[CdK(D`*Q9yyF{9X?#=Pov Df<dC}[H^N(i!~X]]Z?68VWbhCSgGu`pekA3B*<');

/**#@-*/

/**
 * WordPress Database Table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix  = 'wp_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the Codex.
 *
 * @link https://codex.wordpress.org/Debugging_in_WordPress
 */
define('WP_DEBUG', false);

/* That's all, stop editing! Happy blogging. */

/** Absolute path to the WordPress directory. */
if ( !defined('ABSPATH') )
	define('ABSPATH', dirname(__FILE__) . '/');

/** Sets up WordPress vars and included files. */
require_once(ABSPATH . 'wp-settings.php');
