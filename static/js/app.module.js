/**
 The apps.module.js file the base file for the angularjs part of the application

 @author Paul Imisi
 @data 29/07/2015
 */

(function () {
    'use strict';

    angular
        .module('yadexApp', [
            'ngRoute',
            'ngSanitize',
            'ngResource',
            'ngCookies',
            'ngMessages',
            'ui.router',
            'ui.bootstrap',
            'angular-storage',
            'angular-jwt'
        ]
    )
        .constant('AUTH_EVENTS', {
            loginSuccess: 'auth-login-success',
            loginFailed: 'auth-login-failed',
            logoutSuccess: 'auth-logout-success',
            sessionTimeout: 'auth-session-timeout',
            notAuthenticated: 'auth-not-authenticated',
            notAuthorized: 'auth-not-authorized'
        })
        .constant('USER_ROLES', {
            all: '*',
            user: 'generalUser',
            administrator: 'administrativeUser',
            guest: 'guestUser'
        })
        .constant('SERVER_LINKS', {
            host: "http://192.168.120.20:8080",
            signUp: "/index.php/user_registration",
            advertiserLogin: "/index.php/user_login/advertiser",
            publisherLogin: "/index.php/user_login/publisher"
        });
})();