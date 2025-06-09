#!/usr/bin/env python3

import json
import requests


def create_categories(data):
    url = 'http://127.0.0.1:8000/categories/'
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(data), headers=headers)
    return response.json()


def create_brands(data):
    url = 'http://127.0.0.1:8000/brands/'
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(data), headers=headers)
    return response.json()

def create_specification(data):
    url = 'http://127.0.0.1:8000/specifications/'
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(data), headers=headers)
    return response.json()
def main():
    report = {}
    with open('data.json', 'r') as f:
        data = json.load(f)
        # if data.get('categories'):
        #     new_categories = [create_categories(category) for category in data['categories']]
        #     report['categories'] = new_categories
        # if data.get('brands'):
        #     new_brands = [create_brands(brand) for brand in data['brands']]
        #     report['brands'] = new_brands
        if data.get('specifications'):
            new_specifications = [create_specification(specification) for specification in data['specifications']]
            report['specifications'] = new_specifications
    with open('report.json', 'w') as f:
        json.dump(report, f, indent=4)
    return "done"

if __name__ == '__main__':
    print(main())