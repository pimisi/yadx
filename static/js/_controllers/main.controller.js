(function (currentScriptPath) {
    'use strict';

    angular.module('yadexApp')
        .config(config)
        .controller('MainController', MainController);

    config.$inject = ['$routeProvider'];

    function config($routeProvider) {
        'use strict';

        $routeProvider
            .when('/', {
                controller: 'MainController',
                templateUrl: '/static/js/_templates/main.home.html'//currentScriptPath.replace('main.controller.js', 'main.home.html')
            }) // Home route
            .when('/blog', {
                controller: 'MainController',
                templateUrl: '/static/js/_templates/main.blog.html'//currentScriptPath.replace('main.controller.js', 'main.blog.html')
            }) // Blog route
            .when('/advertisers', {
                controller: 'MainController',
                templateUrl: '/static/js/_templates/main.advertiser.html'//currentScriptPath.replace('main.controller.js', 'main.advertiser.html')
            }) // Blog route
            .when('/publishers', {
                controller: 'MainController',
                templateUrl: '/static/js/_templates/main.publisher.html'//currentScriptPath.replace('main.controller.js', 'main.publisher.html')
            }) // Blog route
            .when('/faqs', {
                controller: 'MainController',
                templateUrl: '/static/js/_templates/main.faqs.html'//currentScriptPath.replace('main.controller.js', 'main.faqs.html')
            }) // Blog route
            .when('/contact-us', {
                controller: 'MainController',
                templateUrl: '/static/js/_templates/main.contact.html'//currentScriptPath.replace('main.controller.js', 'main.contact.html')
            }) // Blog route
            .otherwise({
                redirectTo: '/'
            })
    }

    MainController.$inject = ['$scope', '$rootScope', '$resource', 'SERVER_LINKS']

    function MainController($scope, $rootScope, $resource, SERVER_LINKS) {

        // Links
        $scope.links = SERVER_LINKS;
        $scope.signInEnabled = false;

        $scope.enableSignIn = function() {
            $scope.signInEnabled = true;
        }

        // get referrer
        var matchPattern = /^http[s]*:\/\/[\w\d\.:]+[\/#]*\/(contact-us)[\/]*/i;

        var currentLocation = document.location.toLocaleString();
        var contactUsMatch = matchPattern.test(currentLocation);

        function handleContactUsRoute() {
            $scope.subjects = [
                {"label": "Complaint", "value": 1},
                {"label": "Enquiry", "value": 2},
                {"label": "Feedback", "value": 3},
                {"label": "Suggestion", "value": 4},
                {"label": "Other", "value": 5}
            ];

            if (!$scope.hasOwnProperty('countries')) {
                $scope.countries = [];
                // Get countries
                $resource('/static/js/_resources/countries.json')
                    .query(function (data) {
                        console.log(data);
                        $scope.countries = data;
                    });
            }


            //$rootScope.contact = {"subject": 'Subject', "country": 'Country'};
            $scope.master = {"subject": 'Subject', "country": 'Country'};
            //$scope.contact = angular.copy($scope.master);

            $scope.selectSubject = function (selectedIndex) {
                $scope.contact.subject = $scope.subjects[selectedIndex]['label'];
                console.log("Selected " + $scope.contact.subject);

                if ($scope.contact.subject.toLowerCase() != "subject") {
                    $scope.contactForm.selSubject.$error.subject = false;
                    $scope.contactForm.selSubject.$valid = true;
                    $scope.contactForm.selSubject.$invalid = false;
                }
            }

            $scope.selectCountry = function (selectedIndex) {
                $scope.contact.country = $scope.countries[selectedIndex]['name'];
                console.log("Selected " +$scope.contact.country);
            }

            $scope.contactForm = {
                "isProcessing": false,
                "completed": false
            };

            $scope.reset = function(form) {
                if (form) {
                    form.$setPristine();
                    form.$setUntouched();
                    $scope.contactForm = form;
                    $scope.contactForm.isProcessing = false;
                    $scope.contactForm.completed = false;
                }

                $scope.contact = angular.copy($scope.master);
            }

            $scope.processForm = function (form) {
                //$scope.subject = $scope.contact.subject;
                // Validate form
                if (form.$valid) {
                    $scope.contactForm = form;
                    $scope.contactForm.isProcessing = true;
                    $scope.alert = {
                        type: 'info',
                        msg: "We are sending your " + $scope.contact.subject + ". Please wait..."
                    }

                    // Make service call
                    var contactUs = $resource('/api/contact', {},
                        {
                            sendMessage: {
                                method:'POST'
                            }
                        });
                    contactUs.sendMessage($scope.contact)
                        .$promise
                        .then(function (data) {

                            var subMessage = "";
                            switch ($scope.contact.subject.toLowerCase()) {
                                case "enquiry": subMessage = " A YAdX representative will get " +
                                    "in-touch with you regarding this as soon as possible";
                                    break;
                                case "complaint": subMessage = " A YAdX representative will get " +
                                    "look into your issue and get back to you as soon as possible";
                                    break
                            }

                            $scope.alert = {
                                type: 'success',
                                msg: "Thank you for your " + $scope.contact.subject + "." + subMessage
                            }
                            $scope.contactForm.completed = true;
                            $scope.contactForm.isProcessing = false;
                        }, function() {
                            console.log("Something happened...");
                            $scope.contactForm.completed = false;
                            $scope.contactForm.isProcessing = false;
                        })
                        .catch(function(data) {
                            $scope.alert = {
                                type: 'danger',
                                msg: data.message
                            }
                            $scope.contactForm.completed = false;
                            $scope.contactForm.isProcessing = false;
                        })
                } else {
                    $scope.contactForm.isProcessing = false;
                    $scope.contactForm.completed = false;
                }

            }

            $scope.closeAlert = function (index) {
                $scope.alerts.splice(index, 1);
            };

            // Initialize the form in a reset state
            $scope.reset();
        }

        if (contactUsMatch) {
            handleContactUsRoute();
        } else {
            // Do these only for the contact us route
            $rootScope.$on('$locationChangeStart', function (event, next, current) {

                var contactUsMatch = matchPattern.test(next);

                if (contactUsMatch) {
                    handleContactUsRoute();
                }
            });
        }


    }

})(
    (function () {
        var scripts = document.getElementsByTagName("script");
        var currentScriptPath = scripts[scripts.length - 1].src;

        return currentScriptPath;
    })()
);