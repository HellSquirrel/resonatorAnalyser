from django.views.generic import View
from analyser.libs.json.jsonParser import convertFromJson, convertToJson
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed


class JSONView(View):

    def __init__(self, **kwargs):
        super(JSONView, self).__init__(**kwargs)
        self.errors = []

    def handleGet(self, data):
        raise NotImplementedError

    def get(self, request):

            requestData = request.GET['params']
            data = convertFromJson(requestData)

            try:
                result = self.handleGet(data)

                return HttpResponse(convertToJson(result), content_type="application/json")

            except NotImplementedError:
                return HttpResponseNotAllowed()

        #converts from json

