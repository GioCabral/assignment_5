from django.shortcuts import render
from .forms import PuzzleForm
import math, random

def puzzle_view(request):
    result = {}
    if request.method == 'POST':
        form = PuzzleForm(request.POST)
        if form.is_valid():
            number = form.cleaned_data['number']
            text = form.cleaned_data['text']

            # Number Puzzle
            if number % 2 == 0:
                result['number_result'] = f"The number {number} is even. Its square root is {math.sqrt(number):.2f}."
            else:
                result['number_result'] = f"The number {number} is odd. Its cube is {number ** 3}."

            # Text Puzzle
            binary = ' '.join(format(ord(c), '08b') for c in text)
            vowels = sum(c.lower() in 'aeiou' for c in text)
            result['text_result'] = f"Binary: {binary}"
            result['vowel_count'] = f"Vowel Count: {vowels}"

            # Treasure Hunt
            secret = random.randint(1, 100)
            attempts = []
            guess = None
            for i in range(1, 6):
                guess = random.randint(1, 100)
                if guess < secret:
                    attempts.append(f"Attempt {i}: {guess} (Too low!)")
                elif guess > secret:
                    attempts.append(f"Attempt {i}: {guess} (Too high!)")
                else:
                    attempts.append(f"Attempt {i}: {guess} (Correct!)")
                    break
            result['treasure'] = attempts
            result['won'] = "You found the treasure!" if guess == secret else "You did not find the treasure."
    else:
        form = PuzzleForm()

    return render(request, 'puzzle/puzzle.html', {'form': form, 'result': result})
