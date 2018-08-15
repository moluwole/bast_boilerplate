let mix 	= require('laravel-mix');
// let elixir  = require('laravel-elixir');


mix.js('public/assets/js/bast.js', 'public/static/js')
   .sass('public/assets/sass/app.scss', 'public/static/css');

// elixir(function(mix) {
//     mix.coffee('public/assets/js/app.coffee', 'public/static/js');
// });