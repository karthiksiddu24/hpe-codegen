// Old JavaScript file (outdated syntax and practices)

var fs = require('fs');

var readFile = function(path, callback) {
    fs.readFile(path, 'utf8', function(err, data) {
        if (err) {
            console.log('Error reading file:', err);
            callback(err);
        } else {
            console.log('File read successfully.');
            callback(null, data);
        }
    });
};

var processFile = function(path) {
    readFile(path, function(err, data) {
        if (err) {
            console.log('Cannot process file.');
        } else {
            console.log('Processing file contents...');
            var lines = data.split('\n');
            for (var i = 0; i < lines.length; i++) {
                console.log('Line ' + (i + 1) + ': ' + lines[i]);
            }
        }
    });
};

// Hardcoded file path for testing
processFile('example.txt');
