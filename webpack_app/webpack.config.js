module.exports = {
    entry: './src/js/app.js',
    output: {
        path: __dirname+'/dist',
        filename: 'bundle.js'
    },
    mode: "development",
    module:{
        rules:[
           {test:/\.js$/, loader:'babel-loader', exclude: /node_modules/, query:{presets:['es2015']}},
           {test:/\.css$/, loader:'style-loader!css-loader'},
        ]
    }
}

/*
// Run the commane webpack app.js -o  bundle.js on cmd in the same root directory.


module.exports = {
    entry: "./app/entry",
    mode: "development",
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                
            }
        ]
    }
};
*/