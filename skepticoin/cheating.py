'''
Generated like so (in skepticoin-repl):

for i in range(0, (coinstate.head().height // 500 + 1) * 500, 500):
    block = coinstate.at_head.block_by_height[i]
    print("""    %-8d: '%s',""" % (block.height, human(block.hash())))
'''

KNOWN_HASHES = {
    0       : '00c4ff1d0788c7058f3d8388d77b2feda0921fa141078fb895871634e0c36780',
    500     : '00786517cfdd81bbab75cc7d9ca738038cab005b0e0a6205b2aa07bfa917db25',
    1000    : '00fefe403e7108adca4f47a05ca59c61c08de1ee644d5d8a23b16b0f187de916',
    1500    : '004367b96c71fa69d931630a43dc60a070abb47c0febfa1b665690d5174a0869',
    2000    : '00c816a7c07d49ad3599c2ccfabf0e5055a0d547ebbc89ec358bb94328b1fef0',
    2500    : '0017f18030825766556c9e48d938092d3671b942c144e3ad84b06416ddabd8f3',
    3000    : '00b896c88866cf585491ef22d7ca42b8e70231815c6c7cc4863bce8a48bf7b83',
    3500    : '0027a1cc062e155cb83c8f47e4f1fd9b800614327c6e004c825793cdc010b5d6',
    4000    : '000b4a2d5ca016ee7f8e48438b139bc196610b379c85a73917c42d8bc06f4008',
    4500    : '00728eb4953a19471e1e0decb2d8b862fdd296740af14aa6db93943c9a786f2d',
    5000    : '0092f95d626f87faeae098b804470932b06ce0fcdded2a6c132078d764562ae4',
    5500    : '00a11402f94e899beab029b85b692f8d3247a3b98df375377f67e7ab6db6792a',
    6000    : '00591fee548a6cd736effe8143944f51e73fa6231ddf950eae92822cf914aa95',
    6500    : '0056e853dd5368797ccf4a9d2277002ca28d4b9c760ca28c2d136857101679fe',
    7000    : '00cae677cb2263dbf387a8232b05a73bd4464a0a559c7ce621934662c26321e0',
    7500    : '0033d2556494c990b83c80328be69aa88c83708d50d0764d2500380652e716b0',
    8000    : '006cf2ce65228fcd159ec63f44e7b666ac5378647342e917a2bb28fdfdbb326d',
    8500    : '001050a19cdfc579cf94811d793b9db54eb357aa98982f8eb6a985f41ab1464f',
    9000    : '0083671511256574b0d570f3143507f667414d150ef67157ab5d1f47a7732b52',
    9500    : '00429f3326540fe6ca64bb71f27785bbda820087c03828604776afe34af0ef94',
    10000   : '00e682c20eb9b53b176f64b33551f46bf03414328828717aae98733ac94e50d1',
    10500   : '00f8ff5cf06468c82ddf2ba5bb129c529496a664ee74a46e36dd6b8738130973',
    11000   : '010305c482e0675e9af8e539dc766a15c33f9e3270643d80b93b8bdd0358dc7b',
    11500   : '01a9fa19ea48c7492ee9a4eaaf86f80449c1c45f4db694642601fa0f959bab63',
    12000   : '008c8d01275a2b2467a4b5f81ffd4e276a323a7595f7043019bcff66dea2d6ba',
    12500   : '01e7366ff56295f9dbef382c35cebc96ea26738615ac23eddc88d8e678647bc6',
    13000   : '019c3834f6b28bef7825426198b0a8e7275d5883f92ab82c293e2e741c9d4908',
    13500   : '000571b36313a0ddf000bfef6daa9806bea85a6404451362fa601e3750245f21',
    14000   : '01316d05404a59ba9665b98e72cf746b80fe3240812edaa44f308cffb703d8fe',
    14500   : '0090f53d8908abaa2393fb7849e32d301ab08862b88a64ed3bd856c9dbf1da57',
    15000   : '015cd3436dcdd70d8999588f34a0d50f6a8ed77bc60fa3992970298b7d1a697a',
    15500   : '01909a27e929ec66cb10cc16c139d567ce64c929b3f2009c8751e50a18c61a85',
    16000   : '015ea1a4adce1cff0b8165e666fa3bcd76818627a510020b70fffbc8707579e4',
    16500   : '0123f7e399a69d35e4e38b33a4ce16b8f5f148e1e570d7386ab939268514fe84',
    17000   : '0097bb6832f6bd146352951bee48606e7ec66c7ffc535e0b8d123a1e72f7f9bb',
    17500   : '019f52e13ebf7fff127b4961dc32df935ed158a9a9163066b95c61cb71bfa403',
    18000   : '00bc834df67129b24bd70ad58a1380e1e7d38e75a55958f5c3b4fff02d134fcd',
    18500   : '00c9a686b830a342b5cba05807ed5affa79fe314b2fb96f4c7133f2fd58ef73e',
    19000   : '0130dc3498df05743b3b9a94a8543a5bb06167d7351b827312508b34bb351014',
    19500   : '0009d7cd29cb773819a90cab06ea63245617783c947b99567e025b5f0735edff',
    20000   : '0068f214398a98fead26716c6d9ff671c6b2cfcc33b58d6e6a8486917906c5de',
    20500   : '007b468c38a0b07216a362ea7ed7c0cb6643fc34a3a00628d395b87c34d14409',
    21000   : '004439061e8e3f2d2c369061231e88bbc4c02527e30257fafba42f3a1a903a58',
    21500   : '001eff9c184ea97bd4ea4c9768ac7a0c3adbcfae74689d398889229b80ebdf11',
    22000   : '00b6f967760291dcf9eae27ba9ba7dcfe187d10ed772e684300824b6477c4ec4',
    22500   : '00c41bb6b00808d2f8d8b62047bb3c96f172cb06e131cf89613f94875aefe306',
    23000   : '00e6adbe165ce035f82bd10f00a6d2cd9a737728d46959b67ef3386a96bcba19',
    23500   : '00514f3253ddfa37bf778bffbca80b249c515dbeb6ee94a9da35af7acd1a2691',
    24000   : '005dccd354d9d12350879f001592e7f686a3f86b2dd7ebaae5e120fbb2f2eec7',
    24500   : '00bee182c7bec6ebac2736118218d381bf32bce6528b9ed0c1d5d8c6e4d599a2',
    25000   : '001e9c22df502c7d9317e3d600fa5cf71817ba5824da0d9c498e7f3ac74f0535',
    25500   : '003458ac1abca1f193519ff9604ba2ba64a9fb439936870fce8e535a49c9d217',
    26000   : '00028c317426c00b1d1754d70d90d358427aab592bb890f6f5c40de6ceabded6',
    26500   : '0045a7b960ade0263ba5351aeb74bb660453672ac3e79ded41a51e0fee4befb9',
    27000   : '003ce08c576daf9048d4bd52a7211334ccbc89539ee64ab5d26026d38757e198',
    27500   : '00ce6e1e68279beee663ee2dc6f3e99b1355df6bf89b6e85f185b408b77d9da0',
    28000   : '0091c96462eec43315b341f85bdee1332483412c55cec58b427ff70209d1e783',
    28500   : '00afd5a7b7437ac5179aef03fc475e40b121a804354d2a27d0dae00222745a85',
    29000   : '000ac21dd0bcb6990d1b926fe2d819db77565bd634bc17e091a63e0f0e3f31f1',
    29500   : '0038e3cee2f151b07856e23cddda2681f03ed18c874f1e0e085a20caaf197507',
    30000   : '008772fe0b1ff4ff6f6e38fffebcca85ab5d1f40cc2d0f438194a9049b02ed87',
    30500   : '0019cd82963914d206df764407b4f953242515054357ca1d86e3e73a513405af',
    31000   : '000efab01b3def16cd202db5c8efdb7d2c1b285308d42f822dec7fe9b352833d',
    31500   : '0008c6d27e887230b4ab777007c5c447bc51c3f78f5aa796a26770c78167f75f',
    32000   : '0004069f3d0d157f9d593dbf7683229946b60d8c164e5d7cbc34e536169713a9',
    32500   : '00117371ac96d314466e112987b84f7e8c5849a95062d23142a1725f1d764286',
    33000   : '001290d9a15bbeb36cb7b0d7fb8d16cf6fce2c8b32f1211503fb956ba811cd01',
    33500   : '0007538ef32f67c8ad3c9a3eccf758590c6333586515e3dcbaff991b28d4e20b',
    34000   : '001c82a11a7c7d53345820bb18681e5e88c337bf0e3644080ea4178e27554d8f',
    34500   : '0020c5a64fe0663ea397cf501399493122a4739e4f461b07337f335ea72d6ea5',
    35000   : '001c938b98526a1b9cd762a445ec227b74ca613883c1169cbd140facefdc44d9',
    35500   : '0006c63553fe4535a1b925119db614585eae8d8d4be7c3e5c5f34a4d12125578',
    36000   : '001dcbc64605201a7ce65c06da46a541d47b6ebc527dbfcd89fcab8ade2baf50',
    36500   : '0015693ff0d962907b43357870dbedf5f3f9b21b94692079d12fcfe5470d061f',
    37000   : '0014733e4df4ed1df4879beefadd95ee6831b08db5da1a6598cd7faeef6787c7',
    37500   : '000f2c2c8e757ffb1edb47228148aab8c5304cc7555b10727e2194b386c0dfea',
    38000   : '0009d7e4be910406d7f0bca60f0fc9f64da1eed2d7848b7c592d6b202c9cc70f',
    38500   : '0016b04e168ff72a9b80aa646478fe32fd64ac682f5d856be629266db9594b50',
    39000   : '001675f660e1e4190ed24b74d8176549c78e6f951e4a7c908af67b7cdb83e1e1',
    39500   : '00134b449cc2f805c20a07d00874bf26437acb79f25f4dec37d57368b1a82e54',
    40000   : '000ed4d95f6a7f1d36e563a4ba77d56b90b4009c765a2463e7c87328673ff015',
    40500   : '000aacff0ca07682871db789eb4085ade315ead5235dd75f31472910da6d46d3',
    41000   : '000632a44748d3dcfa1c809747a2bdd6be702eeb48f7295c9196c6ba33b7177a',
    41500   : '0005f4cad67bde2cf944197d56ae30f5b369673cd57486d09c9d4189d2e8bf1a',
    42000   : '000a0313cae86293c5e2ca57ca5e86805d63779137af07befe3996b35a947274',
    42500   : '00028d624e0958bb46b2a3bafe6ea43247f62bc7e23049caad4d2ec68b664d8a',
    43000   : '000a836709382528ae32b4ee69ea4c3577b3b5b8f19a06908ee1e196a33145ce',
    43500   : '000b52b3e4bf7240abf29837571775413bb2ba3f4180bac51b8e36217a6a5758',
    44000   : '0006a771fcf3fd77824af393e89a1805de02ef5f80f2b55c4fca62a5aa0ca52e',
    44500   : '0009789beaa10ff240f7c15fc37536279b619c52d073becb716cac7673063505',
    45000   : '00087aa516a5bacf0ccf1aeb39ab404512d4b66dada014f7c3b8f7a4551564c3',
}

MAX_KNOWN_HASH_HEIGHT = max(KNOWN_HASHES.keys())
