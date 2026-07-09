def abbrev_name(name) :
    return ".".join(word[0].upper() for word in name.split())
abbrev_name("Sam Harris")
abbrev_name("patrick feeney")