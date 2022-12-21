from django.http import HttpResponse
from .person_repository import person_repository
from .person import Person
from .person_exceptions import PersonException
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

__person_repository = person_repository()


def __сheck_inputs(inputs, requires):
    for param in requires:
        if param not in inputs:
            raise Exception(json.dumps({'status': 'data_error', 'message': f'{param} expected'}), 400)
    return 'passed'


def start_page(request):
    return HttpResponse('You are welcome at training project "django_ws_orm"')


def get_users_profile(request):
    return JsonResponse(__person_repository.get(), safe=False)


@csrf_exempt
def get_delete_put_user_profile(request, id):
    if request.method == 'GET':
        return HttpResponse(__person_repository.get(Person(id=id)))

    elif request.method == 'DELETE':
        if __person_repository.delete(Person(id=id)):
            return HttpResponse(json.dumps({'success': True}), 200)
        else:
            raise PersonException('Не удалось выполнить запрос')

    elif request.method == 'PUT':
        inputs = json.loads(request.body)
        check = __сheck_inputs(inputs, ['name', 'age'])
        if check != 'passed':
            return check
        name = inputs["name"]
        age = inputs["age"]
        if __person_repository.update(Person(id, name, age)):
            return HttpResponse(json.dumps({'success': True}), 200)
        else:
            raise PersonException('Не удалось выполнить запрос')


@csrf_exempt
def post_user_profile(request):
    inputs = json.loads(request.body)
    check = __сheck_inputs(inputs, ['name', 'age'])
    if check != 'passed':
        return check
    name = inputs["name"]
    age = inputs["age"]
    return HttpResponse(__person_repository.create(Person(name=name, age=age)))


