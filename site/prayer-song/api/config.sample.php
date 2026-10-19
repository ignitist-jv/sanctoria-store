<?php
// Copy to config.php on the server and fill in. config.php is gitignored and
// denied over HTTP. Anything left out falls back to the defaults in lib.php.
return [
    'base_url'       => 'https://sanctoriastore.com/prayer-song',
    'items'          => ['prayersong-1' => 'song'],     // ClickBank item numbers for this offer
    'elevenlabs_key' => '',                            // makes the music
    'anthropic_key'  => '',                            // Claude: writes the lyrics
    'mock'           => false,
    'mail'           => [
        'driver'   => 'kit',                            // kit | log | resend | postmark
        'api_key'  => '',
        'from'     => 'Sanctoria <songs@sanctoriastore.com>',
        'reply_to' => 'support@sanctoriastore.com',
    ],
    'admin_email'    => '',                             // where "needs review" alerts go
    'admin_hash'     => '',                             // the admin page password, hashed. Make it with:  php -r 'echo password_hash(readline("Password: "), PASSWORD_DEFAULT), "\n";'
    'kit'            => ['tag_lead' => null, 'tag_buyer' => null,
                         'seq_ready' => 2917156,          // Kit sequence "Sanctoria Prayer Song: delivery (song is ready)"
                         'seq_delay' => 2917157],         // Kit sequence "Sanctoria Prayer Song: taking a little longer"
];
