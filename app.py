from flask import Flask, request, jsonify
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)
# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

@app.route('/')
def home():
    return "Server is running!"

@app.route('/compare', methods=['POST'])
def compare():
    data = request.json['numbers']
    arr = list(map(int, data.split(',')))

    arr1 = arr.copy()
    arr2 = arr.copy()

    start = time.time()
    bubble_sort(arr1)
    bubble_time = time.time() - start

    start = time.time()
    merge_sort(arr2)
    merge_time = time.time() - start

    return jsonify({
        "bubble_time": round(bubble_time, 6),
        "merge_time": round(merge_time, 6)
    })

if __name__ == "__main__":
    app.run(debug=True)