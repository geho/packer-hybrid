# Hybridcore Templates Spec Gaps

Open items to revisit after in-flight changes merge:

1. **OS Image Variants**
   - Define variant naming scheme, directory layout, metadata fields, manifests, and validation/testing expectations.
2. **Checksum caching/invalidation**
   - Clarify storage, reuse, and invalidation triggers for checksum caches.
3. **Metadata schema completeness**
   - Enumerate required metadata fields (provisioners, configs, scripts, dependencies, variant info).
4. **Change-detection signals**
   - Specify how manifest/HCL diffs and metadata timestamps block partial updates.
5. **State/repo sync**
   - Detail integration between builder manifests and `hybridcore.state`, including validation commands.
