
let app = {};


let init = (app) => {

    app.data = {
        word: '',// get random word that does not drawn by user
    };

    app.enumerate = (a) => {
        let k = 0;
        a.map((e) => { e._idx = k++; });
        return a;
    };

    app.methods = {
        saveAndConfirm: (word) => {
            window.saveCanvas(word);
            confirm('You have saved the canvas. Please return to the Homepage');
        },
    };

    app.vue = new Vue({
        el: "#vue-target",
        data: app.data,
        methods: app.methods
    });

    app.init = () => {
        axios.get('/getWords')
        .then(function(r) {
            app.vue.word = r.data.word;
            console.log(app.vue.word)
        })
        .catch(error => {
            console.error(error);
        });
    };

    app.init();
};

init(app);
