  *	?????!?@2F
Iterator::ModelU???N@??!;R?<??R@)D?l?????1T#?Y._R@:Preprocessing2f
/Iterator::Model::ParallelMapV2::Zip[0]::FlatMap4??7????!|???*@)?H?}8??1O???%@:Preprocessing2u
>Iterator::Model::ParallelMapV2::Zip[0]::FlatMap::Prefetch::Map?}8gD??!??W??! @)RI??&¶?1%"?JC@:Preprocessing2?
LIterator::Model::ParallelMapV2::Zip[0]::FlatMap::Prefetch::Map::FiniteRepeatZd;?O???!4?%@)?J?4??1?b???@:Preprocessing2U
Iterator::Model::ParallelMapV2'?Wʢ?!??E_<?@)'?Wʢ?1??E_<?@:Preprocessing2v
?Iterator::Model::ParallelMapV2::Zip[0]::FlatMap[4]::Concatenate?HP???!?:7??W??)tF??_??1???>	???:Preprocessing2l
5Iterator::Model::ParallelMapV2::Zip[1]::ForeverRepeat?|a2U??!?b?#ބ??)?5?;Nё?1?{?p????:Preprocessing2Z
#Iterator::Model::ParallelMapV2::Zipa??+e??!$?^'?@0@)ŏ1w-!??1o'??}??:Preprocessing2x
AIterator::Model::ParallelMapV2::Zip[1]::ForeverRepeat::FromTensorV-???!	?of????)V-???1	?of????:Preprocessing2v
?Iterator::Model::ParallelMapV2::Zip[0]::FlatMap[5]::Concatenate?HP???!?:7??W??)??ZӼ???1?SQ???:Preprocessing2p
9Iterator::Model::ParallelMapV2::Zip[0]::FlatMap::PrefetchS?!?uq{?!"f??ɣ??)S?!?uq{?1"f??ɣ??:Preprocessing2?
SIterator::Model::ParallelMapV2::Zip[0]::FlatMap::Prefetch::Map::FiniteRepeat::Range?????g?!դ??2??)?????g?1դ??2??:Preprocessing2?
NIterator::Model::ParallelMapV2::Zip[0]::FlatMap[5]::Concatenate[1]::FromTensor??_?LU?!Ly7?H???)??_?LU?1Ly7?H???:Preprocessing2?
OIterator::Model::ParallelMapV2::Zip[0]::FlatMap[5]::Concatenate[0]::TensorSliceǺ???F?!R???&n??)Ǻ???F?1R???&n??:Preprocessing2?
NIterator::Model::ParallelMapV2::Zip[0]::FlatMap[4]::Concatenate[1]::FromTensora2U0*?C?!F\?jj^??)a2U0*?C?1F\?jj^??:Preprocessing:?
]Enqueuing data: you may want to combine small input data chunks into fewer but larger chunks.
?Data preprocessing: you may increase num_parallel_calls in <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map" target="_blank">Dataset map()</a> or preprocess the data OFFLINE.
?Reading data from files in advance: you may tune parameters in the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch size</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave cycle_length</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer_size</a>)
?Reading data from files on demand: you should read data IN ADVANCE using the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer</a>)
?Other data reading or processing: you may consider using the <a href="https://www.tensorflow.org/programmers_guide/datasets" target="_blank">tf.data API</a> (if you are not using it now)?
:type.googleapis.com/tensorflow.profiler.BottleneckAnalysisk
unknownTNo step time measured. Therefore we cannot tell where the performance bottleneck is.no*noZno#You may skip the rest of this page.BZ
@type.googleapis.com/tensorflow.profiler.GenericStepTimeBreakdown
  " * 2 : B J R Z b JGPUb??No step marker observed and hence the step time is unknown. This may happen if (1) training steps are not instrumented (e.g., if you are not using Keras) or (2) the profiling duration is shorter than the step time. For (1), you need to add step instrumentation; for (2), you may try to profile longer.