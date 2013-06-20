angular.module('culpa', [])
    .controller("CulpaController", function ($scope) {
        var events = [
            {type: "IMPROVING", timestamp : 1234567889, instigator: "jalie", message: "First culpa-event ever!", project: "PRTR"},
            {type: "GRAVE", timestamp : 1234567900, instigator: "jalie", message: "Breaks the build!", project: "PRTR"},
            {type: "GRAVE", timestamp : 1234567950, instigator: "jalie", message: "Coverage went down by 3%!", project: "PRTR", link: "https://www.confluence.com/bla"},
            {type: "INFORMATIVE", timestamp : 1234567950, instigator: "jalie", message: "Coverage went down by 3%!", project: "PRTR", link: "https://www.confluence.com/bla"}
        ]
        $scope.events = events;
        $scope.remove = function (index) {
            $scope.events.splice(index, 1);
        }
    });
