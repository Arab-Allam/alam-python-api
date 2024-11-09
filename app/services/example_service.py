import os
import numpy as np
import pandas as pd
import pyarabic.araby as araby
from ibm_watsonx_ai.foundation_models import Model

def main(sentence, word, irab):
    print(sentence, word, irab)



    def get_credentials():
        return {
            "url": "https://eu-de.ml.cloud.ibm.com",
            "apikey": "vGt-8Abv5RGFaVdJ8OvBibAMOCZCMp1Vgg8kdkn0zbtd"
        }

    model_id = "sdaia/allam-1-13b-instruct"
    parameters = {
        "decoding_method": "greedy",
        "max_new_tokens": 900,
        "repetition_penalty": 1
    }
    project_id = 'c2974d6b-cb61-4859-a34e-e5943a1e919c'

    model = Model(
        model_id=model_id,
        params=parameters,
        credentials=get_credentials(),
        project_id=project_id,
        space_id=None
    )

    def prompt_input():
        few_shots = """
<s> [INST]
        الجمله: ما أهملت واجبى قط
        الاعراب: ما : اسم إن منصوب وعلامة نصبه الألف
 [/INST]
 خاطئ
الإعراب الصحيح: ما: اسم نكرة مبني على السكون في محل رفع مبتدأ
</s><s> [INST]
الجمله: الطائر يطير في السماء
الاعراب : يطير : فعل مضارع مرفوع وعلامة رفعه الضمة الظاهرة على آخره،والفاعل ضمير مستتر تقديره "هو" يعود على الطائر
[/INST]
صحيح
</s><s> [INST]
الجمله: الذي يفوز فله جائزة
الاعراب: يفوز : فعل مضارع مرفوع،وعلامة رفعه الضمة الظاهرة على آخره
[/INST]
صحيح
</s><s> [INST]
الجمله: كل من تلقاه يشكو دهره
الاعراب: يشكو : فعل مضارع مرفوع وعلامة رفعه الضمة المقدرة على الواو للثقل،والفاعل ضمير مستتر تقديره "هو"
 [/INST]
صحيح
</s><s> [INST]
الجمله: خرج القطار من المحطة
الاعراب: المحطة : مفعول لأجله مرفوع وعلامة رفعه الضمة
[/INST]
خاطئ
الاعراب الصحيح: المحطة: مفعول به منصوب وعلامة نصبه الفتحة
</s><s> [INST]
الجمله: دائما أحب والدى
الاعراب: والدي : توكيد منصوب وعلامة نصبه الكسرة
[/INST]
خاطئ
الإعراب الصحيح: والدي: مفعول به منصوب وعلامة نصبه الفتحة
</s><s> [INST]
الجمله: دائما أحب والدى
الإعراب : أحب : خبر كان منصوب وعلامة نصبه حذف النون
[/INST]
خاطئ
الإعراب الصحيح:أحب: فعل مضارع مرفوع وعلامة رفعه الضمة.
</s><s> [INST]
الجمله: دائما أحب والدى
الإعراب: دائما : مفعول مطلق مجرور وعلامة جره الكسرة
[/INST]
خاطئ
الإعراب الصحيح: دائما: ظرف زمان منصوب وعلامة نصبه الفتحة
</s><s> [INST]
الجمله: الأولاد يلعبون في الحديقة
الاعراب: الحديقة : حرف جر مبني على السكون
[/INST]
خاطئ
الإعراب الصحيح: الحديقة : اسم مجرور وعلامة جره الكسرة الظاهرة على آخره
<s></s> [INST]
الجمله: الأولاد يلعبون في الحديقة
الاعراب: في : عطف بيان مجرور وعلامة جره الفتحة
[/INST]
خاطئ
الإعراب الصحيح: حرف جر
</s>"""

        return few_shots
 

    def analyze_sentence(sentence, word, irab):
        generated_response = []
        question = f"""
        الجمله: {sentence}
        الاعراب: {word} : {irab}"""        
        question = f"""
        <s> [INST] {prompt_input()}
        {question}
        [/INST]        

        """
        final_result = model.generate_text(prompt=question, guardrails=False)
        
     
        not_correct = ['خاطئ', 'غير صحيح', 'خطأ','خطا','التصحيح']
        if any(item in final_result for item in not_correct):
         generated_response.append(0)

        elif "صحيح" in final_result:
            generated_response.append(1)
        else:
            generated_response.append(2)
        
        return generated_response[-1], final_result
    return analyze_sentence(sentence, word, irab)