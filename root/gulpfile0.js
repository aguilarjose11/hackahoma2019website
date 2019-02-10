// Here be Dragons!

/* Dependency declaration */
var gulp            = require('gulp');                  // Script & enviroment manager.
var browserSync     = require('browser-sync').create(); // Front-end Development tool.

/* Task declarations */



/**
 * function to move javascript files from the node.js modules
 * into the JavaScript folder (/src/js)
 */
gulp.task('js', function() {
    // gets the files to be moved.
    return gulp.src(['node_modules/bootstrap/dist/js/bootstrap.min.js', 'node_modules/jquery/dist/jquery.min.js', 'node_modules/popper.js/dist/popper.js'])
        .pipe(gulp.dest("./js"))          // sets the destination folder for the selected files (Js).
        .pipe(browserSync.stream());        // updates and restarts the static server.
});

/**
 *  function for static server & watch sass & html files for changes.
 */
gulp.task('serve', function() {
    // begins the static server.
    browserSync.init({
        server: "./"  // Change if the code folder path changes!
    });

    // Change if code folder path changes
    gulp.watch("src/*.html").on('change', browserSync.reload); // reloads the entire static server.
});

/**
  * Default task that is run when the gulp command is called.
  * The task will run the js and serve tasks, see above for more info.
  */
gulp.task('default', ['js', 'serve']);
