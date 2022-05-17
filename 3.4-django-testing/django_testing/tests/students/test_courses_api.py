import pytest
from rest_framework.test import APIClient
from model_bakery import baker
from students.models import Course, Student


# def test_example():
#     assert False, "Just test example"


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def courses_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory


@pytest.fixture
def students():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory


@pytest.mark.django_db
def test_get_one_course(client, courses_factory, students):
    courses = courses_factory()

    response = client.get('/api/v1/courses/')

    assert response.status_code == 200
    data = response.json()
    assert data[0]['name'] == courses.name


@pytest.mark.django_db
def test_get_courses(client, courses_factory, students):
    courses = courses_factory(_quantity=20)

    response = client.get('/api/v1/courses/')

    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(courses)
    for i, c in enumerate(data):
        assert c['name'] == courses[i].name


@pytest.mark.django_db
def test_id_filter(client, courses_factory, students):
    courses = courses_factory(_quantity=20)
    course_id = courses[0].id

    response = client.get('/api/v1/courses/', data={'id': course_id})

    assert response.status_code == 200
    data = response.json()
    assert data[0]['name'] == Course.objects.get(id=course_id).name


@pytest.mark.django_db
def test_name_filter(client, courses_factory, students):
    courses = courses_factory(_quantity=20)
    course_name = courses[0].name

    response = client.get('/api/v1/courses/', data={'name': course_name})

    assert response.status_code == 200
    data = response.json()
    assert data[0]['id'] == Course.objects.get(name=course_name).id


@pytest.mark.django_db
def test_create_course(client, courses_factory, students):
    Course.objects.create(id='10', name='DjangoCourse')

    response = client.get('/api/v1/courses/', id='10')

    assert response.status_code == 200
    data = response.json()
    assert data[0]['name'] == 'DjangoCourse'


@pytest.mark.django_db
def test_update_course(client, courses_factory, students):
    courses = courses_factory(_quantity=20)
    course_id = courses[0].id

    patch_response = client.patch(path='/api/v1/courses/'+str(course_id)+'/', data={'name': 'DjangoCourse'},)

    assert patch_response.status_code == 200

    get_response = client.get(path='/api/v1/courses/'+str(course_id)+'/')
    assert get_response.status_code == 200

    data = get_response.json()
    assert data['name'] == 'DjangoCourse'


@pytest.mark.django_db
def test_delete_course(client, courses_factory, students):
    courses = courses_factory(_quantity=20)
    course_id = courses[0].id

    delete_response = client.delete(path='/api/v1/courses/'+str(course_id)+'/')

    assert delete_response.status_code == 204

    get_response = client.get(path='/api/v1/courses/'+str(course_id)+'/')
    assert get_response.status_code == 404
