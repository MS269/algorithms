# Heap(힙)

우선, 힙은 우선순위 큐를 위해서 만들어졌다.

## Priority Queue(우선순위 큐)

데이터들이 우선 순위를 가지고 있으며, 우선 순위가 높은 데이터가 큐에서 먼저 빠져 나간다.

배열, 연결 리스트 그리고 힙으로 구현 가능하며, 힙이 가장 효율적이다.

### 언제 사용?

- 시뮬레이션 시스템
- 작업 스케줄링
- 수치해석 계산

### 시간 복잡도

힙을 사용했을 때,

- 삽입: O(logn)
- 삭제: O(logn)

## 힙 개념

배열을 기반으로 한 Complete Binary Tree(완전 이진 트리)의 일종으로, 여러 값 중 최대값과 최소값을 빠르게 찾아내도록 만들어진 자료구조이다.

- Max Heap(최대 힙): 각 노드의 값이 자식 노드의 값보다 크거나 같은 완전 이진 트리이다.
- Min Heap(최소 힙): 각 노드의 값이 자식 노드의 값보다 작거나 같은 완전 이진 트리이다.

최대/최소 힙에서 루트 노드에 있는 값이 제일 크므로, 최대/최소 값을 찾는 데 O(1)의 시간 복잡도가 소요된다.

힙 트리는 중복된 값을 허용한다(이진 탐색 트리는 중복된 값 허용 x).

## 힙 구현

배열을 기반으로 구현하며, 첫번째 인덱스는 사용하지 않는다.

인덱스는 i번째 노드에 대하여 왼쪽 자식은 i x 2, 오른쪽 자식은 i x 2 + 1이다.

### 삽입

1. 마지막 노드에 새로운 노드를 삽입
2. 새로운 노드를 부모 노드들과 교환

### 삭제

1. 최대값(루트 노드) 삭제(최대 힙에서 삭제 연산은 최대값을 삭제하는 것)
2. 삭제된 루트 노드를 마지막 노드로 교환
3. Heapify(힙을 재구성)