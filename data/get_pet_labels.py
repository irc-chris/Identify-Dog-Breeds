#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#
# PROGRAMMER: Ishawnia Christopher
# DATE CREATED: June 27, 2024
# REVISED DATE: July 1, 2024
# PURPOSE: Create the function get_pet_labels that creates the pet labels from
#          the image's filename. This function inputs:
#           - The Image Folder as image_dir within get_pet_labels function and
#             as in_arg.dir for the function call within the main function.
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main.
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir


# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create
#       with this function
#
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames
    of the image files. These pet image labels are used to check the accuracy
    of the labels that are returned by the classifier function, since the
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Replace None with the results_dic dictionary that you created with this
    # function
    all_files = listdir(image_dir)
    results_dic = {}

    # Iterate through all files in the directory
    for file_name in all_files:

        # Make sure it's not a dot file and 
        if not file_name.startswith('.'):
            # Check it's not a duplicate label
            if file_name not in results_dic:
                # Get alphabetical components and join them by spaces.
                label = " ".join([word.strip() for word in file_name.split("_") if word.isalpha()])

                # Store lowercase label in dictionary
                results_dic[file_name] = [label.lower()]
            else:
                print(
                    "** Warning: Key=",
                    file_name,
                    "already exists in results_dic with value =",
                    results_dic[file_name],
                )

    # Return dictionary
    return results_dic
