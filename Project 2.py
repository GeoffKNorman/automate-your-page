EXAMPLE_LIST_OF_CONCEPTS = [ ['Previous Examples of Code', 
'''In begining this second project, I had an understanding of for loops, while loops, string indexing and concatenation, but I had no idea how we were going to produce HTML tags around our text.  
I was relieved to know that we would learn something useful to do this but I was horrified by the first exercises where we had to perform string matching to slice apart a giant block of text to create our notes like so:
def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = + \'\'\'
<div class="concept">
    <div class="concept-title">
        \'\'\' + concept_title
    html_text_2 = \'\'\'
    </div>
    <div class="concept-description">
        \'\'\' + concept_description
    html_text_3 = \'\'\'
    </div>
</div>\'\'\'
    
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def get_title(concept):
    start_location = concept.find('TITLE:')
    end_location = concept.find('DESCRIPTION:')
    title = concept[start_location+7 : end_location-1]
    return title

def get_description(concept):
    start_location = concept.find('DESCRIPTION:')
    description = concept[start_location+13 :]
    return description

def get_concept_by_number(text, concept_number):
    counter = 0
    while counter < concept_number:
        counter = counter + 1
        next_concept_start = text.find('TITLE:')
        next_concept_end   = text.find('TITLE:', next_concept_start + 1)
        if next_concept_end >= 0:
            concept = text[next_concept_start:next_concept_end]
        else:
            next_concept_end = len(text)
            concept = text[next_concept_start:]
        text = text[next_concept_end:]
    return concept

TEST_TEXT = \"\"\"TITLE: Why Computers are Stupid
DESCRIPTION: The phrase "computers are stupid" refers 
to how they interpret instructions literally. This 
means that small typos can cause big problems.
TITLE: Python
DESCRIPTION: Python is a "programming language." It 
provides programmers a way to write instructions for a 
computer to execute in a way that the computer can understand.
TITLE: While Loops
DESCRIPTION: A while loop repeatedly executes the body of
the loop until the "test condition" is no longer true.\"\"\"


def generate_all_html(text):
    current_concept_number = 1
    concept = get_concept_by_number(text, current_concept_number)
    all_html = ''
    while concept != '':
        title = get_title(concept)
        description = get_description(concept)
        concept_html = generate_concept_HTML(title, description)
        all_html = all_html + concept_html
        current_concept_number = current_concept_number + 1
        concept = get_concept_by_number(text, current_concept_number)
    return all_html
''', "lesson-4-1"],
                             ['A better way using Lists!', '''Using lists, we learned how to take less steps in separating out our content and I realized I could automate the generation of the html for my sublists by adding an extra list item after my content.  
                             Being very lazy on my part, I decided just to copy over the output from my python file instead of pasting in all the previous content into the python list (because that would have taken forever and I would rather learn sometehing new) and make a few tweaks once I had placed my content safely in my HTML document.  
                             A few tweaks here and there, and realizing that I hadn't added an h2 tag to beginning of this new section, nor had I thought to nest my content even further to include headers and the section heading around my content... I made the changes manually to save time and submit my project and move on.  

                             Really glad to learn about nesting lists and calling individual elements through [] indexing and for loops. <p> Here is the better way of using these procedures to wrap our notes in HTML tags:</p> 

def generate_concept_HTML(concept_title, concept_description, lesson_id):
    html_text_1 = \'\'\'
<div class="concept">
    <div class="concept-title",\'\'\' + "<id=" + lesson_id + ">"+ concept_title 
    html_text_2 = \'\'\'
    </div>
    <div class="concept-description">
        \'\'\' + concept_description
    html_text_3 = \'\''\
    </div>
</div>\'\'\'
    
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def make_HTML(concept):
    concept_title = concept[0]
    concept_description = concept[1]
    lesson_id = concept[2]
    return generate_concept_HTML(concept_title, concept_description, lesson_id)

# This is an example of what a list of concepts might look like.

def TOCmaker(concept):
    concept_title = concept[0]
    concept_description = concept[1]
    lesson_id = concept[2]
    list_html = \'\'\'
    <li><a href="#\'\'\' lesson_id + \'\'\'">\'\'\' + concept_title + \'\'\'</a></li>\'\'\'
    return list_html


# This is the function you will write.
def make_HTML_for_many_concepts(list_of_concepts):
    list_of_TOC = ''
    many_HTML = ''
    for concept in list_of_concepts:
        many_HTML += make_HTML(concept)
        list_of_TOC += TOCmaker(concept)


    return many_HTML
    return list_of_TOC

# This is an example of what a list of concepts might look like.
EXAMPLE_LIST_OF_CONCEPTS = [ ['Python', 'Python is a Programming Language', lesson_id=lesson-4-1],
                             ['For Loop', 'For Loops allow you to iterate over lists'lesson_id=lesson-4-2],
                             ['Lists', 'Lists are sequences of data'lesson_id=lesson-4-3] ]

# This is the function you will write.
def make_HTML_for_many_concepts(list_of_concepts):
    many_HTML = ''
    for i in list_of_concepts:
        many_HTML += make_HTML(i)
    return many_HTML
        
    # write code here that generates the appropriate HTML
    # for a list of concepts.

print make_HTML_for_many_concepts(EXAMPLE_LIST_OF_CONCEPTS)



                             ''',"lesson-4-2"]]

def generate_concept_HTML(concept_title, concept_description, lesson_id):
    concept_description = concept_description.replace('<', ' &lt; ')
    concept_description = concept_description.replace('>', ' &gt; ')
    concept_description = concept_description.replace('\n', '<br />')

    html_text_1 = '''
<div class="concept">
    <div class="concept-title "''' + ''' id="''' + lesson_id + '''">'''+ concept_title 
    html_text_2 = '''
    </div>
    <div class="concept-description">
        ''' + concept_description
    html_text_3 = '''
    </div>
</div>'''
    
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def make_HTML(concept):
    concept_title = concept[0]
    concept_description = concept[1]
    lesson_id = concept[2]
    return generate_concept_HTML(concept_title, concept_description, lesson_id)

# This is an example of what a list of concepts might look like.

def TOCmaker(concept):
    concept_title = concept[0]
    concept_description = concept[1]
    lesson_id = concept[2]
    list_html = '''
    <li><a href="#''' + lesson_id + '''">''' + concept_title + '''</a></li>'''
    return list_html


# This is the function you will write.
def make_HTML_for_many_concepts(list_of_concepts):
    list_of_TOC = ''
    many_HTML = ''
    for concept in list_of_concepts:
        many_HTML += make_HTML(concept)
        list_of_TOC += TOCmaker(concept)
    return many_HTML

def make_TOC_for_many_concepts(list_of_concepts):
    list_of_TOC = ''
    for concept in list_of_concepts:
        list_of_TOC += TOCmaker(concept)
    return list_of_TOC


    # write code here that generates the appropriate HTML
    # for a list of concepts.

print make_HTML_for_many_concepts(EXAMPLE_LIST_OF_CONCEPTS)
print make_TOC_for_many_concepts(EXAMPLE_LIST_OF_CONCEPTS)

