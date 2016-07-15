var app = angular.module('newSurvey', []);

app.controller('newSurveyCtrl',['$scope', '$http','$window', function ($scope, $http, $window){

    var counter = 0;
    var ocounter = 0;
    $scope.surveyName=""
    $scope.questions = [{qid:counter, questionName : '',
                        options : [{oid:0, optionName:''}]}];

    $scope.addQuestion = function (){
        counter++;
        ocounter++;
        newQuestion ={qid:counter, questionName :'', options:[{oid:ocounter,optionName:''}]};
        $scope.questions.push(newQuestion);
    }

    $scope.addOption = function(qid){
        ocounter++
        var i = 0;
        for(i=0;i<$scope.questions.length;i++){
            if ($scope.questions[i].qid===qid){
                newOption = {oid:ocounter, optionName:''}
                $scope.questions[i].options.push(newOption);
                break;
            }
        }

    };

    $scope.removeOption = function(qid, oid){
        var i=0;
        for(i=0;i<$scope.questions.length;i++){
            if($scope.questions[i].qid===qid){
                var j=0;
                for(j=0;j<$scope.questions[i].options.length;j++){
                    if($scope.questions[i].options[j].oid===oid){
                        $scope.questions[i].options.splice(j,1);
                    }
                }
            }
        }
    };

    $scope.removeQuestion = function(qid){
        var i=0;
        for(i=0;i<$scope.questions.length;i++){
            if($scope.questions[i].qid===qid){
                $scope.questions.splice(i,1);
            }
        }
    };

    $scope.disableSave= function(){
        if ($scope.surveyName.length == 0){
            return true
        }
        if ($scope.questions.length<1){
            return true;
        }
        var i =0;
        for(i=0;i<$scope.questions.length;i++){
            if($scope.questions[i].options.length<2 || $scope.questions[i].questionName.length == 0){
                return true;
            }
            var j =0;
            for(j =0; j<$scope.questions[i].options.length; j++){
                if($scope.questions[i].options[j].optionName.length ==0){
                    return true;
                }
            }

        }

        return false;
    };

    //save survey. ajax call to post the form for processing on server.
    $scope.saveSurvey = function(){
        var request = $http({
            method:"POST",
            url:"/save",
            data:JSON.stringify({
                surveyName:$scope.surveyName,
                questions:$scope.questions}),
            headers: { 'Content-Type': 'application/json' }
        });

        request.success(function(data){
            console.log(data)
            $window.location.href= '/surveys'
        });
    };

// end of controller
}]);