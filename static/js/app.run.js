(function () {
    angular
        .module('yadexApp')
        .run(run);

    run.$inject = [
        '$templateRequest',
    ];

    function run($templateRequest) {
        $templateRequest('/static/js/_templates/main.home.html');
        $templateRequest('/static/js/_templates/main.advertiser.html');
        $templateRequest('/static/js/_templates/main.publisher.html');
        $templateRequest('/static/js/_templates/main.contact.html');
        $templateRequest('/static/js/_templates/main.faqs.html');
        $templateRequest('/static/js/_templates/main.blog.html');
    }

})();