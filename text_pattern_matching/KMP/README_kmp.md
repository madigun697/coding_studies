## Knuth-Morris-Pratt(KMP) Algorithm

### KMP 알고리즘이란

* KMP Algorithm 이란 기존의 Navie Pattern Matching 알고리즘의 비효율성을 개선한 알고리즘
  * 기존 Naive Pattern Matching의 경우 모든 Index에서의 Subset과 입력된 Pattern을 비교함으로써 비교가 필요없는 Subset까지도 비교하는 비효율적인 작업이 발생
  * 이를 회피하고자 Pattern이 일치하지 않는 Subset 구간을 전부 Skip 하는 방식을 사용하는 경우 Pattern과 일치하는 일부 Subset 이 누락
* KMP Algorithm은 기존 방식에서 발생하는 위의 2가지 문제를 개선하는 방법을 Prefix와 Suffix를 이용하여 해결
  ```  python
  # Example
  pattern = 'ABBABABB'
  text = 'ABBACAABBABABBABABC'
  ```

  * Prefix: 특정 문자열을 앞에서부터 절단한 Subset 

      |  0   |  1   |  2   |  3   |  4   |  5   |  6   |  7   |
      | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
      |  A   |      |      |      |      |      |      |      |
      |  A   |  B   |      |      |      |      |      |      |
      |  A   |  B   |  B   |      |      |      |      |      |
      |  A   |  B   |  B   |  A   |      |      |      |      |
      |  A   |  B   |  B   |  A   |  B   |      |      |      |
      |  A   |  B   |  B   |  A   |  B   |  A   |      |      |
      |  A   |  B   |  B   |  A   |  B   |  A   |  B   |      |
      |  A   |  B   |  B   |  A   |  B   |  A   |  B   |  B   |

  * Suffix: 특정 문자열을 뒤에서부터 절단한 Subset

      |  0   |  1   |  2   |  3   |  4   |  5   |  6   |  7   |
      | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
      |      |      |      |      |      |      |      |  B   |
      |      |      |      |      |      |      |  B   |  B   |
      |      |      |      |      |      |  A   |  B   |  B   |
      |      |      |      |      |  B   |  A   |  B   |  B   |
      |      |      |      |  A   |  B   |  A   |  B   |  B   |
      |      |      |  B   |  A   |  B   |  A   |  B   |  B   |
      |      |  B   |  B   |  A   |  B   |  A   |  B   |  B   |
      |  A   |  B   |  B   |  A   |  B   |  A   |  B   |  B   |

  * KMP Algorithm에서는 Pattern의 Subset 들에서 Prefix와 Suffix가 동일한 가장 긴 Subset의 길이를 찾음 (Pi)

    * ex) Example pattern(ABBABABB)에서 length가 4인 Subset(ABBA) -> 일치하는 구간 없음: 0

      |      | Prefix |      |      | Suffix |      |      |
      | :--: | :----: | :--: | :--: | :----: | :--: | :--: |
      |  0   |   A    |      |      |        |      |  A   |
      |  1   |   A    |  B   |      |        |  B   |  A   |
      |  2   |   A    |  B   |  B   |   B    |  B   |  A   |

    * ex) Example pattern(ABBABABB)에서 length가 5인 Subset(ABBAB) -> 일치하는 구간 존재: 1

      |       | Prefixx |       |      |      | Suffix |      |       |       |
      | :---: | :-----: | :---: | :--: | :--: | :----: | :--: | :---: | :---: |
      |   0   |    A    |       |      |      |        |      |       |   B   |
      | **1** |  **A**  | **B** |      |      |        |      | **A** | **B** |
      |   2   |    A    |   B   |  B   |      |        |  B   |   A   |   B   |
      |   3   |    A    |   B   |  B   |  A   |   B    |  B   |   A   |   B   |

    * 모든 Subset에 대해 일치하는 구간의 길이를 구한 결과

    ``` python
    pi = [0, 0, 0, 1, 2, 1, 2, 3]
    ```

  * 기존 Naive Pattern Matching과 동일하게 매 Index 에서의 Subset과 Pattern을 비교하지만 비교한 다음 사용된 Pattern의 Pi 값만큼 Skip하여 불필요한 비교 연산을 제외

      * 아래 표를 참고하면 13번째 iteration에서 Pattern과 일치하는 Subset을 찾은 뒤 Subset 다음으로 Skip하거나 Index를 1만 증가시키는 형태가 아니라, ABBABABB의 B의 pi인 3을 찾아 pi[3]의 index로 pattern을 이동
          ABBABABB의 B의 index는 7, pi[7] = 3, pattern[3] = A => 14번째 iteration에서는 ABBA부터 비교 시작

      * | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    | 9    | 10   | 11   | 12   | 13   | 14   | 15   | 16   | 17   | 18   | 19   |
          | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
          | A    | B    | B    | A    | C    | A    | A    | B    | B    | A    | B    | A    | B    | B    | A    | B    | A    | B    | C    |
          | A    |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |
          | A    | B    |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |
          | A    | B    | B    |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |
          | A    | B    | B    | A    |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |
          |      |      |      | A    |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |
          |      |      |      |      | A    |      |      |      |      |      |      |      |      |      |      |      |      |      |      |
          |      |      |      |      |      | A    |      |      |      |      |      |      |      |      |      |      |      |      |      |
          |      |      |      |      |      | A    | B    |      |      |      |      |      |      |      |      |      |      |      |      |
          |      |      |      |      |      | A    | B    | B    |      |      |      |      |      |      |      |      |      |      |      |
          |      |      |      |      |      | A    | B    | B    | A    |      |      |      |      |      |      |      |      |      |      |
          |      |      |      |      |      | A    | B    | B    | A    | B    |      |      |      |      |      |      |      |      |      |
          |      |      |      |      |      | A    | B    | B    | A    | B    | A    |      |      |      |      |      |      |      |      |
          |      |      |      |      |      | A    | B    | B    | A    | B    | A    | B    |      |      |      |      |      |      |      |
          |      |      |      |      |      | A    | B    | B    | A    | B    | **A** | **B** | **B** |      |      |      |      |      |      |
          |      |      |      |      |      |      |      |      |      |      | **A** | **B** | **B** | A    |      |      |      |      |      |
          |      |      |      |      |      |      |      |      |      |      | A    | B    | B    | A    | B    |      |      |      |      |
          |      |      |      |      |      |      |      |      |      |      | A    | B    | B    | A    | B    | A    |      |      |      |
          |      |      |      |      |      |      |      |      |      |      | A    | B    | B    | A    | B    | A    | B    |      |      |
          | | | | | | | | | | |  |  |  |  |  |  |  | A | |
          | | | | | | | | | | |  |  |  |  |  |  |  |  | A |

### 구현

#### getPi(pattern)

1. pattern의 모든 subset에 대한 iteration 수행
2. 각 subset의 prefix, suffix를 비교
   * 동일한 경우: 해당 prefix(혹은 suffix)의 길이를 pi에 저장
   * 동일하지 않은 경우: prefix, suffix의 길이를 줄여가면서 반복
   * prefix, suffix의 길이가 0인경우: pi에 0 저장
#### patternSearch(text, pattern)

1. getPi(pattern) 을 수행하여 Skipping Inner iteration Map 생성
2. text의 각 character에 대해 iteration 수행
3. pattern의 j번째 자리의 character와 text의 charater를 비교
   * j가 0인경우 다음 step으로 이동
   * character가 서로 다른 경우 j를 pi[j]로 이동 후 다시 비교
   * character가 서로 동일한 경우
      * pattern의 j번째 자리가 마지막인 경우: pattern 찾음
      * pattern의 j번재 자리가 마지막이 아닌 경우: j를 1 증가시킨 뒤 다음 character 비교

### Usage

```python
import pmat_kmp

pattern = 'ABBABABB'
text = 'ABBACAABBABABBABABC'

result = pmat_kmp.patternSearch(text, pattern)
# result = [13]

for o in out:
    print(text[o-len(pattern):o+1])

# ABBABABB
```



### References

* http://bowbowbow.tistory.com/6
* https://www.ics.uci.edu/~eppstein/161/960227.html
* http://mygumi.tistory.com/61
* http://carstart.tistory.com/143



