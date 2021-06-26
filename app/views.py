import datetime

from flask import jsonify, request, g
from flask_restful import Resource, reqparse, fields, marshal_with

from app.models import db

vegetable_fields = {'name':fields.String,
                'price':fields.Float,
                'info':fields.String,
               }
fruit_fields = {'kind':fields.String,
                'name':fields.String,
                'price':fields.Float
}
vegetable_answer_fields = {'status':fields.String,
                  'msg':fields.String,
                  'data':fields.List(fields.Nested(vegetable_fields))
                 }
fruit_answer_fields = {'status':fields.String,
                  'msg':fields.String,
                  'data':fields.List(fields.Nested(fruit_fields))

}
class Vegetable(Resource):
    def __init__(self):
        self.collection = db.vegetable
    @marshal_with(vegetable_answer_fields)
    def get(self):
        paser = reqparse.RequestParser()
        paser.add_argument('name',type=str,required = False)
        paser.add_argument('date',type=str,required=False,default=str(datetime.date.today()))
        args = paser.parse_args()
        a = args.get('name')
        b = args.get('date')
        # print(b)
        # print(a)
        if not a:
            res = self.collection.find({'date':b},{'_id':0})
        else:
            res = self.collection.find({'name':a,'date':b},{'_id':0})

        # print(res)
        result = []
        for i in res:
            # print(i)
            result.append(i)
        if result:
            return {'status':'200 OK',
                  'msg':'查询成功',
                  'data':result,
                 }
        else:
            return {'status':'400 Failed',
                  'msg':'无对应记录',
                  'data':result,
                 }
class Fruit(Resource):
    def __init__(self):
        self.collection = db.fruit
    @marshal_with(fruit_answer_fields)
    def get(self):
        paser = reqparse.RequestParser()
        paser.add_argument('kind',type=str,required=False)
        paser.add_argument('date',type=str,required=False,default=str(datetime.date.today()))
        args = paser.parse_args()
        a = args.get('kind')
        b = args.get('date')
        if not a:
            res = self.collection.find({'date':b},{'_id':0})
        else:
            res = self.collection.find({'kind':{'$regex':(a)},'date':b},{'_id':0})
        # print(res)
        result = []
        for i in res:
            # print(i)
            result.append(i)
        if result:
            return {'status':'200 OK',
                  'msg':'查询成功',
                  'data':result,
                 }
        else:
            return {'status':'400 Failed',
                  'msg':'无对应记录',
                  'data':result,
                 }