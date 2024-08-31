from random import choice
from tqdm import tqdm


def random_sample(dataset, num=5):
    for i in tqdm(range(num)):
        random_sample = choice(range(len(dataset)))
        print(f"Sample {i+1}")
        print("=" * 70)
        print(dataset[random_sample]['text'])
        print()