const express = require( "express" );
const app = express();
const path = require( 'path' );

// EJS
app.use( express.static( path.join( __dirname, 'public' ) ) );
app.set( 'view engine', 'ejs' );
app.set( 'views', path.join( __dirname, '/views' ) );

// Configuration
app.use( express.static( 'public' ) );

// Subpage path
app.get( '/p/:subpage', (req, res) => {
    const { subpage } = req.params;
    res.render( 'subpage', { subpage } );
} );

// Subpage2 path
app.get( '/p/:subpage/:subpage2', (req, res) => {
    const { subpage, subpage2 } = req.params;
    res.send( `You are now browsing the ${ subpage2 } page of ${ subpage }` );
} );

// Home page
app.get( '/p', (req, res) => {
    res.render( 'index.ejs' );
} );

// Contacts
app.get( '/contact', (req, res) => {
    res.send( "Please contact at: " );
} );

// Library
app.get( '/library', (req, res) => {
    res.send( "What book are you looking to read?" );
} );

// Query Strings
app.get( '/search', (req, res) => {
    const { q } = req.query;
    if ( !q ) {
        res.send( "NOTHING FOUND, IF NOTHING SEARCHED!" );
    }
    res.send( `<h1>Search for: ${ q }</h1>` );
} );

// Unknown path
app.get( '*', (req, res) => {
    res.send( "Path not familiar." );
} );

// Port
app.listen( 3000, () => {
    console.log( "LISTENING ON PORT 3000!" );
} );



// Comments
// app.post( '/lib', (req, res) => {
//     res.send( "POST REQUEST!" );
// } );

// app.use( (req, res) => {
//     console.log( "WE GOT A NEW REQUEST!" );
//     // res.send( "HELLO, WE GOT YOUR REQUEST! THIS IS OUR RESPONSE!" );
//     // res.send( '<h1>THIS IS MY WEBPAGE!</h1>' );
// } ); 