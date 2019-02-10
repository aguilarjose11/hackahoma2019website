// Here be Dragons!

/* Dependency declaration */
var gulp            = require('gulp');                  // Script & enviroment manager.
var browserSync     = require('browser-sync').create(); // Front-end Development tool.

/* Task declarations */

/**
 * function to recompile changed files and update them in the-
 * static server (browserSync) to facilitate front-end development.
 */
gulp.task('sass', function(){
    return gulp.src(['node_modules/bootstrap/scss/bootstrap.css']) // gets the files to be compiled. (bootstrap.css & any .sass files)
        .pipe(gulp.dest("./static/css"))                                                    // sets the destination folder.
        .pipe(browserSync.stream());                                                   // updates the browserSync to restart the static server and show the changes.
});

/**
 * function to move javascript files from the node.js modules
 * into the JavaScript folder (/src/js)
 */
gulp.task('js', function() {
    // gets the files to be moved.
    return gulp.src(['node_modules/bootstrap/dist/js/bootstrap.min.js', 'node_modules/jquery/dist/jquery.min.js', 'node_modules/popper.js/dist/popper.js'])
        .pipe(gulp.dest("./static/js"))          // sets the destination folder for the selected files (Js).
        .pipe(browserSync.stream());        // updates and restarts the static server.
});

/**
 *  function for static server & watch sass & html files for changes.
 */


/**
  * Default task that is run when the gulp command is called.
  * The task will run the js and serve tasks, see above for more info.
  */
gulp.task('default', ['js', 'sass']);
