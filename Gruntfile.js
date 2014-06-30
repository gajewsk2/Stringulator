// Generated on 2014-06-26 using generator-angular 0.9.1
'use strict';


// # Globbing
// for performance reasons we're only matching one level down:
// 'test/spec/{,*/}*.js'
// use this if you want to recursively match all subfolders:
// 'test/spec/**/*.js'
var isDirty = false;
function toggleDebug() {

}
module.exports = function (grunt) {

  // Load grunt tasks automatically
  require('load-grunt-tasks')(grunt);

  // Time how long tasks take. Can help when optimizing build times
  require('time-grunt')(grunt);


  // Define the configuration for all the tasks
  grunt.initConfig({

    // Project settings
    stringulator: {
      root: 'stringulator',
      static: 'stringulator/static',
      dist: 'dist',
      templates: 'stringulator/templates'
    },

    // Watches files for changes and runs tasks based on the changed files
    watch: {
      bower: {
        files: ['bower.json'],
        tasks: ['wiredep']
      },
      js: {
        files: ['<%= stringulator.static %>/scripts/**/{,*/}*.js'],
        tasks: ['newer:jshint:all']
      },
      compass: {
        files: ['<%= stringulator.static %>/styles/{,*/}*.{scss,sass}'],
        tasks: ['autoprefixer']
      },
      gruntfile: {
        files: ['Gruntfile.js']
      }
    },

    // Make sure code styles are up to par and there are no obvious mistakes
    jshint: {
      options: {
        jshintrc: '.jshintrc',
        reporter: require('jshint-stylish'),
        force: true
      },
      all: {
        src: [
          'Gruntfile.js',
          '<%= stringulator.static %>/scripts/{,*/}*.js'
        ]
      }
    },

    // Empties folders to start fresh
    clean: {
      dist: {
        files: [
          {
            dot: true,
            src: [
              '.tmp',
              '<%= stringulator.dist %>/{,*/}*',
              '!<%= stringulator.dist %>/.git*'
            ]
          }
        ]
      },
      cleanup: {
        files: [
          {
            dot: true,
            src: [
              '.tmp'
            ]
          }
        ]
      }
    },

    // Add vendor prefixed styles
    autoprefixer: {
      options: {
        browsers: ['last 1 version']
      },
      dist: {
        files: [
          {
            expand: true,
            cwd: '.tmp/styles/',
            src: '{,*/}*.css',
            dest: '.tmp/styles/'
          }
        ]
      }
    },

    // Automatically inject Bower components into the app
    wiredep: {
      options: {
        cwd: '<%= stringulator.templates %>'
      },
      templates: {
        src: ['<%= stringulator.templates %>/base.html'],
        ignorePath: /..\//
      },
      sass: {
        src: ['<%= stringulator.static %>/styles/{,*/}*.{scss,sass}'],
        ignorePath: /(\.\.\/){1,2}bower_components\//
      }
    },

    // Compiles Sass to CSS and generates necessary files if requested
    compass: {
      options: {
        sassDir: '<%= stringulator.static %>/styles',
        cssDir: '<%= stringulator.static %>/styles/css',
        generatedImagesDir: '<%= stringulator.static %>/images/generated',
        imagesDir: '<%= stringulator.static %>/images',
        javascriptsDir: '<%= stringulator.static %>/scripts',
        fontsDir: '<%= stringulator.static %>/styles/fonts',
        importPath: 'bower_components',
        httpImagesPath: '/images',
        httpGeneratedImagesPath: '/images/generated',
        httpFontsPath: '/styles/fonts',
        relativeAssets: false,
        assetCacheBuster: false,
        raw: 'Sass::Script::Number.precision = 10\n'
      },
      dist: {
        options: {
          generatedImagesDir: '<%= stringulator.dist %>/images/generated'
        }
      }
    },

    cssmin: {
      minify: {

        src: '.tmp/styles/stringulator.css',
        dest: '<%= stringulator.dist %>/styles/stringulator.min.css'
      }
    },
    uglify: {
      body: {
        files: {
          '<%= stringulator.dist %>/scripts/stringulator.min.js': [
            '.tmp/scripts/stringulator.js'
          ]
        }
      }
    },
    concat: {
      head: {
        src: ['<%= stringulator.static %>/scripts/head/*.js'],
        dest: '<%= stringulator.dist %>/scripts/head.js'
      },
      body: {
        src: ['<%= stringulator.static %>/scripts/**/*.js',
          '!<%= stringulator.static %>/scripts/head/*.js'],
        dest: '.tmp/scripts/stringulator.js'
      },
      css: {
        src: ['<%= stringulator.static %>/styles/**/*.css'],
        dest: '.tmp/styles/stringulator.css'
      }
    },

    imagemin: {
      dist: {
        files: [
          {
            expand: true,
            cwd: '<%= stringulator.static %>/images',
            src: '**/*.{png,jpg,jpeg,gif}',
            dest: '<%= stringulator.dist %>/images'
          }
        ]
      }
    },

    svgmin: {
      dist: {
        files: [
          {
            expand: true,
            cwd: '<%= stringulator.static %>/images',
            src: '{,*/}*.svg',
            dest: '<%= stringulator.dist %>/images'
          }
        ]
      }
    },

    htmlmin: {
      dist: {
        options: {
          collapseWhitespace: true,
          conservativeCollapse: true,
          collapseBooleanAttributes: true,
          removeCommentsFromCDATA: true,
          removeOptionalTags: true
        },
        files: [
          {
            expand: true,
            cwd: '<%= stringulator.dist %>',
            src: ['*.html', 'templates/{,*/}*.html'],
            dest: '<%= stringulator.dist %>'
          }
        ]
      }
    },

    // Replace Google CDN references
    cdnify: {
      dist: {
        html: ['<%= stringulator.templates %>/**/*.html']
      }
    },

    // Copies remaining files to places other tasks can use
    copy: {
      dist: {
        files: [
          {
            expand: true,
            dot: true,
            cwd: '<%= stringulator.static %>',
            dest: '<%= stringulator.dist %>',
            src: [
              'admin/**/*',
              'styles/fonts/**/*'
            ]
          },
          {
            expand: true,
            cwd: '.tmp/images',
            dest: '<%= stringulator.dist %>/images',
            src: ['generated/*']
          }
        ]
      },
      styles: {
        expand: true,
        cwd: '<%= stringulator.static %>/styles',
        dest: '.tmp/styles/',
        src: '{,*/}*.css'
      }
    },

    // Run some tasks in parallel to speed up the build process
    concurrent: {
      dist: [
        'compass:dist',
        'imagemin',
        'svgmin'
      ],
      debugFalse: [
        'replace:djangoFalse',
        'replace:sassFalse'
      ],
      debugToggle: [
        'replace:djangoToggle',
        'replace:sassToggle'
      ]
    },
    aws: grunt.file.readJSON('aws-keys.json'),
    s3: {
      options: {
        accessKeyId: '<%= aws.accessKeyId %>',
        secretAccessKey: '<%= aws.secretAccessKey %>',
        bucket: 'stringulator-production',
        access: 'public-read'
      },
      deployStatic: {
        cwd: 'dist/',
        src: '**',
        dest: 'static/'
      }
    },
    replace: {
      djangoToggle: {
        options: {
          patterns: [
            {
              match: 'DEBUG = False',
              replacement: function () {
                isDirty = true;
                return 'DEBUG = True';
              }
            },
            {
              match: 'DEBUG = True',
              replacement: function () {
                if (isDirty) {
                  return 'DEBUG = True';
                }
                isDirty = false;
                return 'DEBUG = False';
              }
            }
          ],
          usePrefix: false
        },
        files: [
          {expand: true, flatten: true,
            src: ['<%= stringulator.root %>/settings.py'],
            dest: '<%= stringulator.root %>/'
          }
        ]
      },
      sassToggle: {
        options: {
          patterns: [
            {
              match: 'debug: false',
              replacement: function () {
                isDirty = true;
                return 'debug: true';
              }
            },
            {
              match: 'debug: true',
              replacement: function () {
                if (isDirty) {
                  return 'debug: true';
                }
                return 'debug: false';
              }
            }
          ],
          usePrefix: false
        },
        files: [
          {expand: true, flatten: true,
            src: ['<%= stringulator.root %>/static/styles/default.scss'],
            dest: '<%= stringulator.root %>/static/styles/'
          }
        ]
      },
      djangoFalse: {
        options: {
          patterns: [
            {
              match: 'DEBUG = True',
              replacement: function () {
                if (isDirty) {
                  return 'DEBUG = True';
                }
                isDirty = false;
                return 'DEBUG = False';
              }
            }
          ],
          usePrefix: false
        },
        files: [
          {expand: true, flatten: true,
            src: ['<%= stringulator.root %>/settings.py'],
            dest: '<%= stringulator.root %>/'
          }
        ]
      },
      sassFalse: {
        options: {
          patterns: [
            {
              match: 'debug: true',
              replacement: function () {
                if (isDirty) {
                  return 'debug: true';
                }
                return 'debug: false';
              }
            }
          ],
          usePrefix: false
        },
        files: [
          {expand: true, flatten: true,
            src: ['<%= stringulator.root %>/static/styles/default.scss'],
            dest: '<%= stringulator.root %>/static/styles/'
          }
        ]
      }

    }
  });

  grunt.registerTask('debug-toggle', [
    'concurrent:debugFalse'
  ]);

  grunt.registerTask('debug-false', [
    'concurrent:debugToggle'
  ]);

  grunt.registerTask('build', [
    'clean:dist',
    'debug-false',
    'concurrent:dist',
    'autoprefixer',
    'concat',
    'cssmin',
    'uglify',
    'copy',
    'debug-toggle'
  ]);

  grunt.registerTask('deploy-static', [
    'build',
    's3',
    'clean:cleanup'
  ]);


  grunt.registerTask('default', [
    'newer:jshint',
    'build',
    'clean:cleanup'
  ]);


};
