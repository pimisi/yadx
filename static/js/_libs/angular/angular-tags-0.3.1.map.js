{"version":3,"file":"dist/angular-tags-0.3.1.min.js","sources":["generated/tags.js"],"names":["angular","module","e","tags","defaultOptions","delimiter","classes","SRC_REGEXP","kc","enter","esc","backspace","kcCompleteTag","kcRemoveTag","kcCancelInput","id","constant","controller","$scope","$timeout","$q","getClasses","tag","r","toggles","selectedTag","selected","forEach","options","klass","groupName","group","_filterSrcTags","idx","srcTags","indexOf","splice","_deletedSrcTags","push","reject","add","i","_add","inputTag","$emit","$id","fail","dfrd","defer","length","name","then","addable","resolve","promise","trust","$sce","trustAsHtml","selectArea","inputActive","remove","directive","$filter","$rootScope","restrict","require","link","scope","element","attrs","ngModel","delimiterRx","RegExp","cancel","$setViewValue","$render","addTag","value","match","addTags","removeLastTag","orderedTags","$viewValue","orderBy","bind","$$phase","$apply","evt","charCodeAt","which","isPropagationStopped","$watch","newVal","focus","$parsers","unshift","values","split","val","$formatters","$document","$parse","decipherTagsOptions","replace","template","model","srcResult","source","tagsWatch","srcWatch","modelWatch","pureStrings","stringArray","defaults","copy","userDefaults","parse","input","Error","itemName","sourceName","viewMapper","modelMapper","watchModel","deletedTag","isDefined","format","watchTags","oldValue","map","isArray","join","arr","isUndefined","isString","item","trim","updateSrc","locals","o","obj","src","$parent","isFunction","isObject","extend","oldVal","$eval","$on","data","$observe","typeaheadOptions"],"mappings":"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","sourceRoot":"/"}